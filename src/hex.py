from math import cos, pi, sin, sqrt

from graphics import Line, Point


class Hex:
    def __init__(self, q, r, s, win=None, size=25, origin=Point(0, 0)) -> None:
        self.size = size
        self.q, self.r, self.s = q, r, s
        assert self.q + self.r + self.s == 0
        self.center = hex_to_pixel(q, r, size, origin)
        self.win = win
        self.has_wall = [True] * 6  # E, NE, NW, W, SW, SE
        self.vertices = []

    def __eq__(self, other) -> bool:
        return self.q == other.q and self.r == other.r and self.s == other.s

    def __ne__(self, other) -> bool:
        return not self == other

    def __add__(self, other):
        return Hex(self.q + other.q, self.r + other.r, self.s + other.s)

    def scale_hex(self, factor):
        return (self.q * factor, self.r * factor, self.s * factor)

    def calc_vertex_offset(self, vertex: int):
        angle = 2 * pi * (vertex + 0.5) / 6
        return Point(self.size * cos(angle), self.size * sin(angle))

    def calc_vertices(self):
        vertices = []
        for i in range(6):
            offset = self.calc_vertex_offset(i)
            vertices.append(Point(self.center.x, self.center.y) + offset)
        return vertices

    def calc_neighbor(self, dir: int):
        return self + self.calc_direction(dir)

    def calc_direction(self, dir: int):
        assert 0 <= dir < 6
        return hex_directions[dir]

    def draw(self):
        self.vertices = self.calc_vertices()
        assert self.win is not None
        for i in range(6):
            fill_color = "white"
            if self.has_wall[i]:
                fill_color = "black"
            self.win.draw_line(
                Line(self.vertices[i], self.vertices[(i + 1) % 6]), fill_color
            )

    def draw_move(self, target, undo=False):
        assert self.win is not None
        fill_color = "red"
        if undo:
            fill_color = "grey"
        self.win.draw_line(Line(self.center, target.center), fill_color)


def pixel_to_hex(hex, point: Point):
    q = (sqrt(3) / 3 * point.x - 1 / 3 * point.y) / hex.size
    r = (2 / 3 * point.y) / hex.size

    return q, r, -q - r


def hex_to_pixel(q, r, size, origin):
    x = size * (sqrt(3) * q + sqrt(3) / 2 * r) + origin.x
    y = size * (3 / 2 * r) + origin.y
    return Point(x, y)


hex_directions = [
    Hex(1, 0, -1),  # E
    Hex(1, -1, 0),  # NE
    Hex(0, -1, 1),  # NW
    Hex(-1, 0, 1),  # W
    Hex(-1, 1, 0),  # SW
    Hex(0, 1, -1),  # SE
]
