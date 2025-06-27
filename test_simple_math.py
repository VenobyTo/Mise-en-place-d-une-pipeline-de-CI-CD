"""Tests unitaires pour la classe SimpleMath."""

import unittest
from simple_math import SimpleMath

class TestSimpleMath(unittest.TestCase):
    """Classe de test pour SimpleMath."""

    def test_addition(self):
        """Teste l'addition."""
        self.assertEqual(SimpleMath.addition(2, 3), 5)

    def test_soustraction(self):
        """Teste la soustraction."""
        self.assertEqual(SimpleMath.soustraction(5, 2), 3)

if __name__ == '__main__':
    unittest.main()