import unittest
import requests

BASE_URL = "http://127.0.0.1:8000"

class TestCalculatorAPI(unittest.TestCase):

    def test_add(self):
        response = requests.get(f"{BASE_URL}/add?a=10&b=5")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"result": 15})

    def test_subtract(self):
        response = requests.get(f"{BASE_URL}/subtract?a=10&b=5")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"result": 5})

    def test_multiply(self):
        response = requests.get(f"{BASE_URL}/multiply?a=10&b=5")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"result": 50})

    def test_divide(self):
        response = requests.get(f"{BASE_URL}/divide?a=10&b=5")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"result": 2})

    def test_divide_by_zero(self):
        response = requests.get(f"{BASE_URL}/divide?a=10&b=0")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"error": "Division by zero is not allowed"})

if __name__ == "__main__":
    unittest.main()