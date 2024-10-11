import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from projet.Rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def setUp(self) -> None:
        print("Mise en place du test")
        self.rectangle = Rectangle(5, 4)

    def tearDown(self) -> None:
        print("Nettoyage du test")

    def test_surface(self):
        self.assertEqual(self.rectangle.surface(), 20)

if __name__ == '__main__':
    unittest.main()