import unittest
import pandas as pd
import os
from job_market.analyzer import JobAnalyzer

class TestJob(unittest.TestCase):
    def setUp(self):

        data = {
            'Title': ['Dev', 'Dev', 'QA'],
            'Salary': [1000, 2000, 3000],
            'Experience': ['MI', 'SE', 'EN'] 
        }
        df = pd.DataFrame(data)
        df.to_csv('test_data.csv', index=False)
        
        self.app = JobAnalyzer('test_data.csv')

    def tearDown(self):

        if os.path.exists('test_data.csv'):
            os.remove('test_data.csv')

    def test_stats(self):

        stats = self.app.get_salary_stats()
        self.assertEqual(stats['avg'], 2000)
        self.assertEqual(stats['min'], 1000)

    def test_top_jobs(self):

        top = self.app.get_top_professions(1)
        self.assertEqual(top.index[0], 'Dev')
        self.assertEqual(top.values[0], 2)

if __name__ == '__main__':
    unittest.main()