# tests/test_app.py
import unittest
from app import create_app

class TestApp(unittest.TestCase):
    
    def setUp(self):
        # Create a test client for our Flask app
        self.client = create_app().test_client()

    def test_hello_world(self):
        # Test the '/' route
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], 'Hello, Kubernetes!')

    def test_info(self):
        # Test the '/info' route
        response = self.client.get('/info')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['name'], 'My Python App')

    def test_items(self):
        # Test the '/items' route
        response = self.client.get('/items')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json['items']), 3)

    def test_get_item(self):
        # Test the '/item/<id>' route with an existing item
        response = self.client.get('/item/2')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['id'], 2)
        self.assertEqual(response.json['name'], 'Item 2')

        # Test with a non-existing item
        response = self.client.get('/item/999')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json['error'], 'Item not found')

    def test_health(self):
        # Test the '/health' route
        response = self.client.get('/health')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['status'], 'Healthy')

if __name__ == '__main__':
    unittest.main()
