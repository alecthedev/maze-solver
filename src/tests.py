import unittest

from graphics import Point, Window
from maze import Maze

window = Window(0, 0)


class Tests(unittest.TestCase):
    def test_spiral_size(self):
        # maze with 4 rings should have 61 hex cells
        m1 = Maze(Point(0, 0), 5, 4, window)
        self.assertEqual(len(m1._hexes), 61)

        # maze with 0 rings should have only 1 cell (the center)
        m2 = Maze(Point(0, 0), 5, 0, window)
        self.assertEqual(len(m2._hexes), 1)


if __name__ == "__main__":
    unittest.main()
