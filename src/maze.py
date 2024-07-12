import random as rand
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
        self._start_pos = (0,0,0)
        self._end_pos = (self._num_rings, 0, -self._num_rings)

        if seed:
            rand.seed(seed)
        self.generate_maze()

    def generate_maze(self):
        self._calc_spiral()
        self._draw_spiral()
        self._open_start()
        self._open_end()
        self._break_walls(self._hexes[self._start_pos])
        
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

    def _draw_spiral(self):
        for hex in self._hexes.values():
            self._draw_hex(hex)

    def _open_start(self):
        start_hex = self._hexes[self._start_pos]    
        start_hex.set_wall(3, False)
        self._draw_hex(start_hex)

    def _open_end(self):
        end_hex = self._hexes[self._end_pos]
        end_hex.set_wall(0, False)
        self._draw_hex(end_hex)

    def _break_walls(self, curr_hex):
            curr_hex.visited = True
            neighbors = curr_hex.calc_all_neighbors()

            rand.shuffle(neighbors)

            for neighbor_pos in neighbors:
                if self._check_neighbor_exists(neighbor_pos):
                    neighbor_hex = self._hexes[neighbor_pos]
                    if not neighbor_hex.visited:
                        self._break_between(curr_hex, neighbor_hex)
                        self._break_walls(neighbor_hex)

    def _check_neighbor_exists(self, hex_pos):
        return hex_pos in self._hexes

    def _get_walls(self, hex_a, hex_b):
        dir = (hex_a.q - hex_b.q, hex_a.r - hex_b.r, hex_a.s - hex_b.s)
        if dir in direction_to_walls:
            wall_a, wall_b = direction_to_walls[dir]
            return wall_a, wall_b
        else:
            return None, None

    def _break_between(self, hex_a, hex_b):
        wall_a, wall_b = self._get_walls(hex_a, hex_b)
        if wall_a is not None and wall_b is not None:
            hex_a.set_wall(wall_a, False)
            hex_b.set_wall(wall_b, False)
        self._draw_hex(hex_a)
        self._draw_hex(hex_b)

    def _draw_hex(self, hex):
        hex.draw()
        self._animate()

    def _animate(self):
        self._win.redraw()
        sleep(0.01)

direction_to_walls = {
    (1, 0, -1): (3, 0),  # Walls = (W/E)
    (1, -1, 0): (4, 1),  # Walls = (SW/NE)
    (0, -1, 1): (5, 2),  # Walls = (SE/NW)
    (-1, 0, 1): (0, 3),  # Walls = (E/W)
    (-1, 1, 0): (1, 4),  # Walls = (NE/SW)
    (0, 1, -1): (2, 5),  # Walls = (NW/SE)
}
