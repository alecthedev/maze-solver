from time import sleep

from graphics import Line, Point, Window
from hex import Hex, hex_directions


class Maze:
    def __init__(self, origin: Point, cell_size: int, num_rings, win: Window):
        self._origin = origin
        self._cell_size = cell_size
        self._num_rings = num_rings
        self._win = win
        self._hexes = []
        self._calc_spiral(num_rings)

    def _calc_spiral(self, num_rings):
        directions = hex_directions
        q, r, s = 0, 0, 0
        self._hexes.append(Hex(q, r, s, self._win, self._cell_size, self._origin))
        for ring in range(num_rings + 1):
            q, r, s = -ring, ring, 0
            for dir in directions:
                for _ in range(ring):
                    q += dir.q
                    r += dir.r
                    s += dir.s
                    self._hexes.append(
                        Hex(q, r, s, self._win, self._cell_size, self._origin)
                    )

        self._draw_spiral()

    def _draw_spiral(self):
        for hex in self._hexes:
            hex.draw()
            self._animate()

    def _animate(self):
        self._win.redraw()
        sleep(0.05)
