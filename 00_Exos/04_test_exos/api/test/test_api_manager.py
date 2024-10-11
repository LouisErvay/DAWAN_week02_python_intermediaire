import unittest
from unittest.mock import patch
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from projet.api_manager import get_user_data

class TestApiManager(unittest.TestCase):

    def setUp(self) -> None:
        print("Mise en place du test")

    def tearDown(self) -> None:
        print("Nettoyage du test")

    @patch("requests.get")
    def test_get_user_data_success(self, mock_get):
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'id': 1, 'name': 'John Doe'}
        mock_get.return_value = mock_response

        result = get_user_data(1)
        self.assertEqual(result, {"id": 1, "name": "John Doe"})
        mock_get.assert_called_once_with("https://api.example.com/user/1")

    @patch('requests.get') 
    def test_get_user_data_failure(self, mock_get):
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        user_data = get_user_data(1)

        self.assertIsNone(user_data)


if __name__ == '__main__':
    unittest.main()