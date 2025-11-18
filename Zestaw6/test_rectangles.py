import unittest
from rectangles import Rectangle
from points import Point

class TestRectangle(unittest.TestCase):

    def test_str(self):
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(str(r), "[(1, 2), (3, 4)]")

    def test_repr(self):
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(repr(r), "Rectangle(1, 2, 3, 4)")

    def test_eq(self):
        r1 = Rectangle(0, 0, 2, 2)
        r2 = Rectangle(0, 0, 2, 2)
        r3 = Rectangle(1, 1, 3, 3)
        self.assertTrue(r1 == r2)
        self.assertFalse(r1 == r3)

    def test_center(self):
        r = Rectangle(0, 0, 2, 2)
        self.assertEqual(r.center(), Point(1, 1))

    def test_area(self):
        r = Rectangle(0, 0, 4, 3)
        self.assertEqual(r.area(), 12)

    def test_move(self):
        r = Rectangle(1, 1, 3, 3)
        r.move(2, -1)
        self.assertEqual(r, Rectangle(3, 0, 5, 2))

if __name__ == "__main__":
    unittest.main()