from math import cos, pi, sin, sqrt

from graphics import Line, Point, Window


class Hex:
    def __init__(self, position: Point, win=None) -> None:
        self.size = 25
        self.q, self.r, self.s = pixel_to_hex(self, position)
        assert self.q + self.r + self.s == 0
        self.center = position
        self.win = win
        self.has_wall = [True] * 6  # E, NE, NW, W, SW, SE
        self.vertices = []

    def __eq__(self, other) -> bool:
        return self.q == other.q and self.r == other.r and self.s == other.s

    def __ne__(self, other) -> bool:
        return not self == other

    def __add__(self, other):
        return Hex(self.q + other.q, self.r + other.r + self.s + other.s)

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
        fill_color = "black"
        if self.has_wall[0]:
            line = Line(self.vertices[0], self.vertices[1])
            self.win.draw_line(line, fill_color)
        if self.has_wall[1]:
            line = Line(self.vertices[1], self.vertices[2])
            self.win.draw_line(line, fill_color)
        if self.has_wall[2]:
            line = Line(self.vertices[2], self.vertices[3])
            self.win.draw_line(line, fill_color)
        if self.has_wall[3]:
            line = Line(self.vertices[3], self.vertices[4])
            self.win.draw_line(line, fill_color)
        if self.has_wall[4]:
            line = Line(self.vertices[4], self.vertices[5])
            self.win.draw_line(line, fill_color)
        if self.has_wall[5]:
            line = Line(self.vertices[5], self.vertices[0])
            self.win.draw_line(line, fill_color)


def pixel_to_hex(hex, point: Point):
    q = (sqrt(3) / 3 * point.x - 1 / 3 * point.y) / hex.size
    r = (2 / 3 * point.y) / hex.size

    return q, r, -q - r


def hex_to_pixel(q, r):
    x = sqrt(3) * q + sqrt(3) / 2 * r
    y = 3 / 2 * r
    return Point(x, y)


hex_directions = [
    Hex(hex_to_pixel(1, 0)),  # E
    Hex(hex_to_pixel(1, -1)),  # NE
    Hex(hex_to_pixel(0, -1)),  # NW
    Hex(hex_to_pixel(-1, 0)),  # W
    Hex(hex_to_pixel(-1, 1)),  # SW
    Hex(hex_to_pixel(0, 1)),  # SE
]
