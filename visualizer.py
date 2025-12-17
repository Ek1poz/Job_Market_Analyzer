import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class JobVisualizer:
    """
    A class to visualize job market data using Matplotlib and Seaborn.
    
    Attributes:
        df (pd.DataFrame): The dataframe containing the job data.
    """

    def __init__(self, dataframe: pd.DataFrame):
        """
        Initializes the visualizer with the data.

        Args:
            dataframe (pd.DataFrame): The cleaned dataframe from JobAnalyzer.
        """
        self.df = dataframe
        sns.set_theme(style="whitegrid")

    def plot_salary_distribution(self):
        """
        Plots the salary distribution histogram with a Kernel Density Estimate (KDE).
        
        Displays a histogram showing the frequency of different salary ranges 
        converted to USD.
        """
        plt.figure(figsize=(12, 6))
        sns.histplot(self.df['salary_in_usd'], kde=True, color='teal')
        
        plt.title('Salary Distribution (USD)')
        plt.xlabel('Salary in USD')
        plt.ylabel('Number of Vacancies')
        plt.ticklabel_format(style='plain', axis='x')
        plt.show()

    def plot_top_jobs(self, n: int):
        """
        Plots a bar chart of the top N most popular job titles.

        Args:
            n (int): The number of top job titles to display.
        """
        top = self.df['job_title'].value_counts().head(n)
        
        plt.figure(figsize=(12, 8))
        sns.barplot(x=top.values, y=top.index, palette='viridis')
        
        plt.title(f'Top-{n} Job Titles')
        plt.xlabel('Number of Vacancies')
        plt.show()

    def plot_salary_by_job(self, n: int):
        """
        Plots salary distribution (boxplot) for the top N jobs.
        
        This visualization helps to identify salary ranges, medians, and outliers
        for the most common job titles.

        Args:
            n (int): The number of top job titles to include in the plot.
        """
        top_jobs = self.df['job_title'].value_counts().head(n).index
        
        df_filtered = self.df[self.df['job_title'].isin(top_jobs)]
        
        plt.figure(figsize=(14, 8))
        
        sns.boxplot(data=df_filtered, x='salary_in_usd', y='job_title', palette='coolwarm')
        
        plt.title(f'Salary Ranges for Top-{n} Professions')
        plt.xlabel('Salary (USD)')
        plt.ylabel('Job Title')
        plt.ticklabel_format(style='plain', axis='x')
        plt.show()

    def plot_experience_salaries(self):
        """
        Plots average salary by experience level.
        
        It automatically decodes experience codes (EN, MI, SE, EX) into 
        human-readable labels (Junior, Middle, Senior, Executive).
        """
        data = self.df.groupby('experience_level')['salary_in_usd'].mean().sort_values()
        
        labels = {'EN': 'Junior', 'MI': 'Middle', 'SE': 'Senior', 'EX': 'Executive'}
        data.index = [labels.get(x, x) for x in data.index]

        plt.figure(figsize=(10, 6))
        sns.barplot(x=data.index, y=data.values, palette='magma')
        
        plt.title('Average Salary by Experience Level')
        plt.ylabel('Salary (USD)')
        plt.xlabel('Experience Level')
        plt.show()
