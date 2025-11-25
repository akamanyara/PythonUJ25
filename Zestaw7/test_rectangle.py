import unittest
from rectangles import Rectangle
from points import Point

class TestRectangle(unittest.TestCase):

    def test_init(self):
        with self.assertRaises(ValueError):
            Rectangle(2, 2, 1, 5)

    def test_str(self):
        self.assertEqual(str(Rectangle(1, 2, 3, 4)), "[(1, 2), (3, 4)]")

    def test_center(self):
        r = Rectangle(0, 0, 4, 4)
        self.assertEqual(r.center(), Point(2, 2))

    def test_area(self):
        self.assertEqual(Rectangle(0, 0, 4, 5).area(), 20)

    def test_move(self):
        r = Rectangle(0, 0, 4, 4).move(1, 2)
        self.assertEqual(r, Rectangle(1, 2, 5, 6))

    def test_intersection(self):
        r1 = Rectangle(0, 0, 4, 4)
        r2 = Rectangle(2, 2, 6, 6)
        self.assertEqual(r1.intersection(r2), Rectangle(2, 2, 4, 4))

    def test_cover(self):
        r1 = Rectangle(0, 0, 4, 4)
        r2 = Rectangle(2, 2, 6, 6)
        self.assertEqual(r1.cover(r2), Rectangle(0, 0, 6, 6))

    def test_make4(self):
        r = Rectangle(0, 0, 4, 4)
        A, B, C, D = r.make4()
        self.assertEqual(A, Rectangle(0, 0, 2, 2))
        self.assertEqual(B, Rectangle(2, 0, 4, 2))
        self.assertEqual(C, Rectangle(2, 2, 4, 4))
        self.assertEqual(D, Rectangle(0, 2, 2, 4))

if __name__ == "__main__":
    unittest.main()