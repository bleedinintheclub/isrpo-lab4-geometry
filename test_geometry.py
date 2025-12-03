import unittest
import time
import math

from geometry import (
    rect_area,
    rect_perimeter,
    rect_diagonal,
    rect_scale,
    circle_area,
    circle_circumference,
    circle_diameter,
    circle_is_unit,
    circle_scale,
)

class GeometryTestCase(unittest.TestCase):
    
    def test_rect_area_normal(self):
        self.assertEqual(rect_area(5, 10), 50)

    def test_rect_area_negative(self):
        self.assertIsNone(rect_area(-3, 10))

    def test_rect_perimeter_normal(self):
        self.assertEqual(rect_perimeter(4, 6), 20)

    def test_rect_diagonal(self):
        self.assertAlmostEqual(rect_diagonal(3, 4), 5.0, places=7)

    def test_rect_scale_positive(self):
        self.assertEqual(rect_scale(2, 3, 4), (8, 12))

    def test_rect_scale_zero_k(self):
        self.assertEqual(rect_scale(5, 7, 0), (0, 0))

    def test_circle_area_normal(self):
        self.assertAlmostEqual(circle_area(3), math.pi * 9, places=7)

    def test_circle_area_negative(self):
        self.assertIsNone(circle_area(-2))

    def test_circle_circumference_normal(self):
        self.assertAlmostEqual(circle_circumference(2), 4 * math.pi, places=7)

    def test_circle_diameter(self):
        self.assertEqual(circle_diameter(5), 10)

    def test_circle_is_unit_true(self):
        self.assertTrue(circle_is_unit(1.0))

    def test_circle_is_unit_false(self):
        self.assertFalse(circle_is_unit(2.0))

    def test_circle_scale_positive(self):
        self.assertEqual(circle_scale(2, 3), 6)

    def test_circle_scale_negative(self):
        self.assertIsNone(circle_scale(-2, 5))



    def test_security_negative_rectangle(self):
        self.assertIsNone(rect_area(-1000, 200))
        self.assertIsNone(rect_perimeter(5, -10))
        self.assertIsNone(rect_scale(-3, 4, 2))

    def test_security_negative_circle(self):
        self.assertIsNone(circle_area(-100))
        self.assertIsNone(circle_circumference(-1))
        self.assertFalse(circle_is_unit(-1))
        self.assertIsNone(circle_scale(3, -2))



    def test_performance_rectangle(self):
        start = time.time()

        for _ in range(300_000):
            rect_area(300, 400)
            rect_perimeter(300, 400)
            rect_diagonal(300, 400)

        duration = time.time() - start
        self.assertLess(duration, 1.5)

    def test_performance_circle(self):
        start = time.time()

        for _ in range(300_000):
            circle_area(300)
            circle_circumference(300)
            circle_diameter(300)

        duration = time.time() - start
        self.assertLess(duration, 1.5)


if __name__ == "__main__":
    unittest.main()