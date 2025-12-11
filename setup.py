from setuptools import setup, find_packages

setup(
    name="job_market",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "matplotlib",
        "seaborn"
    ],
    author="Student Name",
    description="Tool for analyzing job market data"
)