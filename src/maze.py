import random as r
from time import sleep

from graphics import Line, Point, Window
from hex import Hex, hex_directions


class Maze:
    def __init__(
        self, origin: Point, cell_size: int, num_rings, win: Window, seed=None
    ):
        self._origin = origin
        self._cell_size = cell_size
        self._num_rings = num_rings
        self._win = win
        self._hexes = {}
        if seed:
            r.seed(seed)
        self._calc_spiral()
        self._create_start_and_end()

    def _create_start_and_end(self):
        # center cell is the start
        center_hex = self._hexes[(0, 0, 0)]
        center_hex.has_wall[r.randint(0, 5)] = False
        center_hex.draw()
        self._animate()

        # select hex from outer ring to be end
        outer_hexes = self._calc_outer_ring()
        end_hex = outer_hexes[r.randint(0, len(outer_hexes) - 1)]
        end_hex.has_wall[r.randint(0, 5)] = False
        end_hex.draw()
        self._animate()

    def _calc_outer_ring(self) -> list[Hex]:
        outer_hexes = []
        q, r, s = -self._num_rings, self._num_rings, 0

        for dir in hex_directions:
            for _ in range(self._num_rings):
                outer_hexes.append(
                    Hex(q, r, s, self._win, self._cell_size, self._origin)
                )
                q += dir.q
                r += dir.r
                s += dir.s

        return outer_hexes

    def _calc_spiral(self):
        directions = hex_directions
        q, r, s = 0, 0, 0
        self._hexes[(q, r, s)] = Hex(q, r, s, self._win, self._cell_size, self._origin)
        for ring in range(self._num_rings + 1):
            q, r, s = -ring, ring, 0
            for dir in directions:
                for _ in range(ring):
                    q += dir.q
                    r += dir.r
                    s += dir.s
                    self._hexes[(q, r, s)] = Hex(
                        q, r, s, self._win, self._cell_size, self._origin
                    )

        self._draw_spiral()

    def _draw_spiral(self):
        for hex in self._hexes:
            self._hexes[hex].draw()
            self._animate()

    def _animate(self):
        self._win.redraw()
        sleep(0.05)
