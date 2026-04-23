import unittest
from my_math import Annual_Compd_Intrst, pow


class TestMathFunctions(unittest.TestCase):

    def test_pow_normal(self):
        self.assertEqual(pow(2, 3), 8)

    def test_pow_edge(self):
        self.assertEqual(pow(5, 0), 1)

    def test_pow_negative(self):
        self.assertEqual(pow(2, -2), 0.25)

    def test_annual_compd_intrst_normal(self):
        self.assertAlmostEqual(Annual_Compd_Intrst(1000, 0.05, 2, 2), 1104.486101181412)

    def test_annual_compd_intrst_edge(self):
        self.assertEqual(Annual_Compd_Intrst(1000, 0.05, 2, 0), 1000)

    def test_annual_compd_intrst_invalid(self):
        self.assertEqual(Annual_Compd_Intrst(-1000, 0.05, 2, 2), "Invalid input")


if __name__ == "__main__":
    unittest.main()
