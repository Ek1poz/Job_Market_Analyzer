import pandas as pd

class JobAnalyzer:
    """
    A class to analyze job market data from CSV files.
    
    Attributes:
        df (pd.DataFrame): The dataframe containing the job data.
    """

    def __init__(self, csv_path):
        """
        Initializes the analyzer, standardizes columns, and loads data.

        Args:
            csv_path (str): The file path to the CSV dataset.

        Raises:
            FileNotFoundError: If the CSV file does not exist.
            ValueError: If the CSV file is missing required columns.
        """
        try:
            self.df = pd.read_csv(csv_path)
            self._standardize_columns()
            

            required_cols = ['job_title', 'salary_in_usd', 'experience_level']
            
            missing = [c for c in required_cols if c not in self.df.columns]
            
 
            if missing:

                raise ValueError(f"CSV file is invalid. Missing required columns: {missing}")
            
            self.df.dropna(subset=required_cols, inplace=True)
            self.df['salary_in_usd'] = pd.to_numeric(self.df['salary_in_usd'], errors='coerce')
            
        except FileNotFoundError:

            raise FileNotFoundError(f"File {csv_path} not found.")

    def _standardize_columns(self):
        """
        Automatically renames columns to standard names based on a synonym map.
        
        It looks for variations like 'salary', 'gross_salary' and converts them 
        to 'salary_in_usd' to ensure the analyzer works with different CSV formats.
        """
        column_map = {
            'job_title': ['job_title', 'title', 'role', 'position'],
            'salary_in_usd': ['salary_in_usd', 'salary', 'salary_usd', 'gross_salary'],
            'experience_level': ['experience_level', 'experience', 'exp_level', 'level']
        }
        existing_cols_lower = {col.lower(): col for col in self.df.columns}
        for target, aliases in column_map.items():
            if target in self.df.columns: continue
            for alias in aliases:
                if alias.lower() in existing_cols_lower:
                    self.df.rename(columns={existing_cols_lower[alias.lower()]: target}, inplace=True)
                    break

    def get_data(self):
        """
        Returns the raw, cleaned DataFrame.

        Returns:
            pd.DataFrame: The internal dataframe used for analysis.
        """
        return self.df

    def get_salary_stats(self):
        """
        Calculates basic salary statistics.

        Returns:
            dict: A dictionary containing 'min', 'max', 'avg', and 'median' salary in USD.
                  Returns an empty dict if the dataframe is empty.
        """
        if self.df.empty: return {}
        return {
            "min": self.df['salary_in_usd'].min(),
            "max": self.df['salary_in_usd'].max(),
            "avg": round(self.df['salary_in_usd'].mean(), 2),
            "median": self.df['salary_in_usd'].median()
        }

    def get_top_professions(self, n):
        """
        Returns the top N most popular job titles.

        Args:
            n (int): The number of top professions to return.

        Returns:
            pd.Series: A series with job titles as index and counts as values.
        """
        return self.df['job_title'].value_counts().head(n)

    def get_salary_stats_table(self):
        """
        Returns salary statistics as a DataFrame for display.

        Returns:
            pd.DataFrame: A dataframe with a single row containing salary stats.
        """
        stats = self.get_salary_stats()
        return pd.DataFrame([stats])

    def get_top_professions_table(self, n):
        """
        Returns top professions formatted as a DataFrame.

        Args:
            n (int): The number of top professions to include.

        Returns:
            pd.DataFrame: A dataframe with columns 'Job Title' and 'Vacancies Count'.
        """
        counts = self.get_top_professions(n)
        df = counts.reset_index()
        df.columns = ['Job Title', 'Vacancies Count']
        return df

    def get_richest_job(self):
        """
        Identifies the single job position with the highest recorded salary.

        Returns:
            pd.DataFrame: A single-row dataframe with Job Title, Salary, and Experience.
        """
        richest = self.df.sort_values(by='salary_in_usd', ascending=False).iloc[0]
        df = pd.DataFrame([richest[['job_title', 'salary_in_usd', 'experience_level']]])
        df.columns = ['Job Title', 'Salary (USD)', 'Experience']
        return df

    def get_experience_stats_table(self):
        """
        Calculates average salary grouped by experience level for the entire dataset.

        Returns:
            pd.DataFrame: A table showing Avg Salary for Junior, Middle, Senior, Executive levels.
        """
        return self._build_experience_table(self.df)

    def get_salary_growth_for_job(self, target_job):
        """
        Calculates average salary growth by experience level for a specific job title.

        Args:
            target_job (str): The job title to analyze (e.g., 'Data Scientist').

        Returns:
            pd.DataFrame: A table with salary stats for the specific job, or None if not found.
        """
        mask = self.df['job_title'] == target_job
        df_filtered = self.df[mask]
        if df_filtered.empty: return None
        return self._build_experience_table(df_filtered)

    def _build_experience_table(self, data_frame):
        """
        Helper method to build an experience statistics table.
        
        It groups data by experience level, sorts them logically (Junior -> Executive),
        and decodes the abbreviations.

        Args:
            data_frame (pd.DataFrame): The data to process.

        Returns:
            pd.DataFrame: Formatted dataframe with 'Experience Level' and 'Avg Salary'.
        """
        stats = data_frame.groupby('experience_level')['salary_in_usd'].mean()
        order = ['EN', 'MI', 'SE', 'EX']
        stats = stats.reindex(order).dropna()
        df = stats.reset_index()
        df.columns = ['Experience Level', 'Avg Salary']
        codes = {'EN': 'Entry-level (Junior)', 'MI': 'Mid-level', 'SE': 'Senior', 'EX': 'Executive'}
        df['Experience Level'] = df['Experience Level'].replace(codes)
        return df
