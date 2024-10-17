import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from projet.Utilisateur import Utilisateur

class TestUtilisateur(unittest.TestCase):

    def setUp(self) -> None:
        print("Mise en place du test")
        self.utilisateur = Utilisateur("Mael", "123456789")

    def tearDown(self) -> None:
        print("Nettoyage du test")

    def test_changer_mot_de_passe(self):
        self.utilisateur.changer_mot_de_passe("123456789", "123456")
        self.assertEqual(self.utilisateur.mot_de_passe, "123456")

        with self.assertRaises(ValueError):
            self.utilisateur.changer_mot_de_passe("123456", "123")
            self.utilisateur.changer_mot_de_passe("1234567890123", "123456")

if __name__ == '__main__':
    unittest.main()