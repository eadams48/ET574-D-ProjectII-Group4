import unittest
from my_math_main import pow, area_of_circle, factorial, Annual_Compd_Intrst

class TestMyMathFunctions(unittest.TestCase):
   
    # ----- area_of_circle -----
    def test_area_of_circle_basic(self):
        self.assertAlmostEqual(area_of_circle(1), 3.14159)
        self.assertAlmostEqual(area_of_circle(0), 0.0)
        self.assertAlmostEqual(area_of_circle(2.5), 19.6349375)

    def test_area_of_circle_bad_inputs(self):
        with self.assertRaises((TypeError, ValueError)):
            area_of_circle(-1)
        with self.assertRaises((TypeError, ValueError)):
            area_of_circle("2") 
    
    def test_area_of_circle_small_radius(self):
        self.assertAlmostEqual(area_of_circle(0.1), 0.03141592653589793)  # π * 0.1²
   
   
    # ----- factorial -----
    def test_factorial_basic(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(10), 3628800)

    def test_factorial_bad_inputs(self):
        with self.assertRaises((TypeError, ValueError)):
            factorial(-1)
        with self.assertRaises((TypeError, ValueError)):
            factorial(3.5)        
        with self.assertRaises((TypeError, ValueError)):
            factorial("7") 
    
    def test_factorial_large_n(self):
        self.assertEqual(factorial(15), 1307674368000)

if __name__ == "__main__":
    unittest.main(verbosity=2)