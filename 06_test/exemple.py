# Métrique : Compléxité cyclomatique
# C'est une mesure de la complexité d'un programme basée sur le nombre de chemins indépendants dans son graphe de contrôle.
# Elle est utilisée pour évaluer la compléxité du code
# Permets de déterminer la difficulté à tester et maintenir le code

# Unitest est un module python de base exclusif aux tests
# Permet :
# 1- Organiser les test
# 2- Assertions
# 3- Fixtures
# 4- Exécution de tests

def addition(a,b):
    return a+b

def division(a,b):
    if b == 0:
        raise ValueError("Division par 0 interdite")
    else:
        return a/b


import unittest

class TestFunctions(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(addition(2,5), 7)
        self.assertEqual(addition(-2,3), 1)

    def test_division(self):
        self.assertEqual(division(10,2),5)

        with self.assertRaises(ValueError):
            division(2,0)

def main():
    unittest.main()

if __name__ == "__main":
    main()