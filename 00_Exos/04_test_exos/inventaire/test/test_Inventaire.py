import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from projet.Inventaire import Inventaire

class TestInventaire(unittest.TestCase):

    def setUp(self) -> None:
        print("Mise en place du test")
        self.inventaire = Inventaire()

    def tearDown(self) -> None:
        print("Nettoyage du test")

    def test_ajouter_produit(self):
        self.inventaire.ajouter_produit("Stylo bleu", 5)
        self.assertEqual(self.inventaire.obtenir_quantite("Stylo bleu"), 5)

    def test_retirer_produit(self):
        self.inventaire.ajouter_produit("Stylo bleu", 5)
        self.inventaire.retirer_produit("Stylo bleu", 1)
        self.assertEqual(self.inventaire.obtenir_quantite("Stylo bleu"), 4)

        with self.assertRaises(ValueError):
            self.inventaire.retirer_produit("Stylo rouge", 1)
            self.inventaire.retirer_produit("Stylo bleu", 10)


if __name__ == '__main__':
    unittest.main()