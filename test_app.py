import unittest

from app import app


class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_total_revenue(self):
        response = self.app.get("/total_revenue")

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.get_json()["total_revenue"], int)

    def test_highest_region(self):
        response = self.app.get("/highest_region")

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.get_json()["region"], str)
        self.assertIsInstance(response.get_json()["total_sales"], int)

if __name__ == "__main__":
    unittest.main()