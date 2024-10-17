import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from projet.Produit import Produit

class TestProduit(unittest.TestCase):

    def setUp(self) -> None:
        print("Mise en place du test")
        self.produit = Produit("Stylo bleu", 3)

        with self.assertRaises(ValueError):
            self.produit = Produit("Stylo rouge", -5)

    def tearDown(self) -> None:
        print("Nettoyage du test")

    def test_appliquer_remise(self):
        self.produit.appliquer_remise(10)
        self.assertEqual(self.produit.get_prix(), 2.7)

        with self.assertRaises(ValueError):
            self.produit.appliquer_remise(115)

if __name__ == '__main__':
    unittest.main()