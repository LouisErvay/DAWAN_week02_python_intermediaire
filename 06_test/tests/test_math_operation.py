# Un fichier de test commence toujours par 'test_' sinon le module unittest ne reconnait pas
import unittest
from projet.math_operation import addition, division

# Une class de test commence toujours par 'Test'
# Elle hérite aussi toujours de la classe TestCase de unittest: 'unittest.TestCase'
class TestMathOperation(unittest.TestCase):
    
    # Une fonction de test doit toujours commencer par test 'test_'
    def test_addition(self):
        self.assertEqual(addition(5, 10), 15)
        self.assertEqual(addition(-1, 1), 0)
        self.assertEqual(addition(0, 0), 0)

    def test_division(self):
        self.assertEqual(division(5, 10), 0.5)
        
        # Instructions pour tester les erreurs
        with self.assertRaises(ZeroDivisionError):
            division(5, 0)


if __name__ == '__main__':
    unittest.main()