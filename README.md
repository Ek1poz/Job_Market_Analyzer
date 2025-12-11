## Author
```
Sventukh Oleksandr
Sheviak Maxym

Lviv Politechnic
System Analysis
Special Programing Languages

```
# Job Market Analyzer 

**Job Market Analyzer** is a Python library designed to analyze and visualize job market trends based on CSV data. It processes job titles and salaries to provide key financial insights and visual statistics.

This project was developed as part of a Calculation-Graphic Work (RGR).

---

##  Project Structure

```text
JobMarketProject/
├── job_market/              # Main Package Source Code
│   ├── __init__.py          # Package initialization
│   ├── analyzer.py          # Data processing logic (Pandas)
│   └── visualizer.py        # Visualization logic (Matplotlib/Seaborn)
│
├── tests/                   # Unit tests
│   └── test_analyzer.py
│
├── ds_salaries.csv          # Dataset (Data Science Job Salaries)
├── example_usage.ipynb      # Jupyter Notebook for demonstration
├── pyproject.toml           # Build configuration
├── setup.py                 # Setup script
└── README.md                # Project documentation
```

## Installation
```
To use this package, you need to install it in editable mode. Run the following command in your terminal from the project root directory:
```

### Bash
```
pip install -e .
```

### Requirements
```
Python 3.8+

pandas

matplotlib

seaborn

```

## Usage
```
The library is designed to be used in Jupyter Notebooks for interactive analysis.
```


### 1. Import the library
```
Python

from job_market import JobAnalyzer, JobVisualizer
```


### 2. Analyze Data
```
Python

# Initialize analyzer with your CSV file
filename = 'ds_salaries.csv'
analyzer = JobAnalyzer(filename)

# Get statistics (Average, Min, Max, Median)
stats = analyzer.get_salary_stats()
# Display stats dataframe
3. Visualize Data
Python

# Initialize visualizer with the processed data
viz = JobVisualizer(analyzer.get_data())

# Plot Salary Distribution Histogram
viz.plot_salary_distribution()

# Plot Top Job Titles Bar Chart
viz.plot_top_jobs(10)
```




## Features
```
Data Cleaning: Automatically handles missing values and ensures salary data is numeric.

Statistical Analysis: Calculates Min, Max, Average, and Median salaries.

Top Professions: Identifies the most in-demand job titles.

Visualization:

Salary Distribution: Histogram with Kernel Density Estimate (KDE).

Top Jobs: Bar chart of the most popular positions.
```






