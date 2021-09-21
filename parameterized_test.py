from triangle import is_triangle
import unittest


class TriangleTest(unittest.TestCase):
    # The list of data values for your tests can be defined:
    # - outside the class (global variable)
    # - as a class variable (like this)
    # - as a local variable inside the test method.
    # Use which ever is most readable.
    valid_triangles = [
        (1, 1, 1),
        (3, 4, 5),
        (3, 4, 6),
        (20, 24, 28),
        (55, 77, 99),
        (7, 9, 14),
        (60, 80, 100)

    ]

    invalid_triangles = [
        (55, 77, 2),
        (5, 4, 33),
        (7, 1, 9),
        (200, 55, 99),
        (0, 0, 0),
        (1, 99, 999999)
    ]

    value_error_triangles = [
        (-1, -5, -9),
        (-4, 4, 10),
        (55, -77, 99),
        (7, 9, -14),
        (-20, -40, 70),
        (-20, 35, -59)
    ]

    def test_valid_triangle(self):
        for a, b, c in self.valid_triangles:
            with self.subTest():
                message = f"sides are ({a},{b},{c})"
                self.assertTrue(is_triangle(a, b, c), message)

    def test_invalid_triangle(self):
        for a, b, c in self.invalid_triangles:
            with self.subTest():
                message = f"sides are ({a},{b},{c})"
                self.assertFalse(is_triangle(a, b, c), message)

    def test_value_error_with_negative_value_triangle(self):
        for a, b, c in self.value_error_triangles:
            with self.subTest():
                with self.assertRaises(ValueError):
                    is_triangle(a, b, c)
