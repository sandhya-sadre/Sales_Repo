# write test cases for app.py
import unittest
from app import app
class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_total_revenue(self):
        response = self.app.get('/total_revenue')
        self.assertEqual(response.status_code, 500)
        data = response.get_json()
        self.assertIn('total_revenue', data)
        self.assertIsInstance(data['total_revenue'], int)
        self.assertGreater(data['total_revenue'], 0)

    def test_highest_region(self):
        response = self.app.get('/highest_region')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('highest_region', data)
        self.assertIn('total_sales', data)
        self.assertIsInstance(data['highest_region'], str)
        self.assertIsInstance(data['total_sales'], int)
        self.assertTrue(len(data['highest_region']) > 0)

