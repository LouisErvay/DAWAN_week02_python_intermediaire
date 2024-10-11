import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from projet.CompteBancaire import CompteBancaire

class TestCompteBancaire(unittest.TestCase):
    
    # Fonction exécutée avant chaque fonction de test
    def setUp(self) -> None:
        print("Mise en place du test")
        self.compte = CompteBancaire("Alice", 100)

    # Fonction exécutée après chaque fonction de test
    def tearDown(self) -> None:
        print("Nettoyage du test")

    def test_depot(self):
        self.compte.depot(50)
        self.assertEqual(self.compte.get_solde(), 150)

        with self.assertRaises(ValueError):
            self.compte.depot(-10)

    def test_retrait(self):
        self.compte.retrait(30)
        self.assertEqual(self.compte.get_solde(), 70)

        with self.assertRaises(ValueError):
            self.compte.retrait(100)

    def test_get_solde(self):
        self.assertEqual(self.compte.get_solde(), 100)

if __name__ == '__main__':
    unittest.main()