import unittest
from stats_calcul import somme, moyenne, ecart_type, mediane

class TestStatsCalcul(unittest.TestCase):
    def test_somme(self):
        self.assertEqual(somme([1, 2, 3, 4]), 10)
    
    def test_moyenne(self):
        self.assertEqual(moyenne([1, 2, 3, 4]), 2.5)
    
    def test_ecart_type(self):
        self.assertAlmostEqual(ecart_type([1, 2, 3, 4]), 1.118, places=3)
    def test_mediane(self):
        self.assertEqual(mediane([1, 2, 3, 4, 5]), 3)

if __name__ == "__main__":
    unittest.main()