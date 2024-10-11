import unittest
from unittest.mock import patch
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from projet.conversion_nb import conversion_nb

class TestDemo(unittest.TestCase):

    def test_conversion_nb_valid(self):
        with patch("builtins.input", return_value="10"):
            self.assertEqual(conversion_nb(), 10)

    def test_conversion_nb_input_invalid(self):
        with patch("builtins.input", return_value="abc"):
            self.assertRaises(ValueError, conversion_nb)

if __name__ == '__main__':
    unittest.main()