import unittest
from iterators import ZeroOne, RandomNESW, WeekdayCycle

class TestIterators(unittest.TestCase):

    def test_zero_one(self):
        it = iter(ZeroOne())
        seq = [next(it) for _ in range(6)]
        self.assertEqual(seq, [0, 1, 0, 1, 0, 1])

    def test_random_nesw(self):
        it = iter(RandomNESW())
        for _ in range(10):
            self.assertIn(next(it), ("N", "E", "S", "W"))

    def test_weekday_cycle(self):
        it = iter(WeekdayCycle())
        seq = [next(it) for _ in range(9)]
        self.assertEqual(seq, [0,1,2,3,4,5,6,0,1])

if __name__ == "__main__":
    unittest.main()