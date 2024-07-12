import unittest

from graphics import Point, Window
from hex import Hex
from maze import Maze

window = Window(0, 0)

m1 = Maze(Point(0, 0), 5, 4, window)
m2 = Maze(Point(0, 0), 5, 0, window)


class Tests(unittest.TestCase):
    def test_spiral_size(self):
        # maze with 4 rings should have 61 hex cells
        self.assertEqual(len(m1._hexes), 61)

        # maze with 0 rings should have only 1 cell (the center)
        self.assertEqual(len(m2._hexes), 1)

    def test_start_cell_wall(self):
        self.assertFalse(m1._hexes[m1._start_pos].get_wall(3))

    def test_end_cell_wall(self):
        self.assertFalse(m1._hexes[m1._end_pos].get_wall(0))


if __name__ == "__main__":
    unittest.main()
