import unittest
from triangles import Triangle
from points import Point

class TestTriangle(unittest.TestCase):

    def test_str(self):
        t = Triangle(0, 0, 1, 0, 0, 1)
        self.assertEqual(str(t), "[(0, 0), (1, 0), (0, 1)]")

    def test_repr(self):
        t = Triangle(0, 0, 1, 0, 0, 1)
        self.assertEqual(repr(t), "Triangle(0, 0, 1, 0, 0, 1)")

    def test_eq(self):
        t1 = Triangle(0, 0, 1, 0, 0, 1)
        t2 = Triangle(1, 0, 0, 1, 0, 0)
        t3 = Triangle(0, 0, 2, 0, 0, 2)
        self.assertTrue(t1 == t2)
        self.assertFalse(t1 == t3)

    def test_center(self):
        t = Triangle(0, 0, 3, 0, 0, 3)
        self.assertEqual(t.center(), Point(1, 1))

    def test_area(self):
        t = Triangle(0, 0, 4, 0, 0, 3)
        self.assertEqual(t.area(), 6)

    def test_move(self):
        t = Triangle(0, 0, 1, 0, 0, 1)
        t.move(2, 3)
        self.assertEqual(
            t,
            Triangle(2, 3, 3, 3, 2, 4)
        )

if __name__ == "__main__":
    unittest.main()