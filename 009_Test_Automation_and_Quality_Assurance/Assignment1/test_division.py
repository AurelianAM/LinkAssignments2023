import unittest
from division import division

class TestDivision(unittest.TestCase):

    def test_division_by_zero(self):
        self.assertRaises(ZeroDivisionError, division, 5, 0)
    
    def test_division_with_strings(self):
        self.assertRaises(TypeError, division, "asdf", 2)
        self.assertRaises(TypeError, division, "asdf", 0)
        self.assertRaises(TypeError, division, 5, "asdf")
        self.assertRaises(TypeError, division, "asdf", "6")

    def test_division_positive_numbers(self):
        self.assertEqual(division(5, 5), 1)
        self.assertEqual(division(0, 5), 0)
        self.assertEqual(division(100, 4), 25)
        self.assertEqual(division(5, 2), 2.5)
        self.assertEqual(division(6.5, 4), 1.625)
        self.assertAlmostEqual(division(2, 3), 0.66666666, places=6)
        self.assertAlmostEqual(division(2.3253,9), 0.25836666, places=6)
        
    
    def test_division_negative_numbers(self):
        self.assertLess(division(5, -2), 0)
        self.assertLess(division(-5, 2), 0)
        self.assertGreater(division(-5, -2), 0)
        self.assertEqual(division(0, -2), 0)

if __name__ == "__main__":
    unittest.main()