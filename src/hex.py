from math import cos, pi, sin, sqrt

from graphics import Line, Point, Window


class Hex:
    def __init__(self, center: Point, win=None) -> None:
        self.size = 25
        self.q, self.r, self.s = pixel_to_hex(self, center)
        assert self.q + self.r + self.s == 0
        self.center = center
        self.win = win
        self.has_wall = [True] * 6  # E, NE, NW, W, SW, SE
        self.vertices = []

    def __eq__(self, other) -> bool:
        return self.q == other.q and self.r == other.r and self.s == other.s

    def __ne__(self, other) -> bool:
        return not self == other

    def __add__(self, other):
        return Hex(self.q + other.q, self.r + other.r + self.s + other.s)

    def calc_vertex_offset(self, vertex: int):
        angle = 2 * pi * (vertex + 0.5) / 6
        return Point(self.size * cos(angle), self.size * sin(angle))

    def calc_vertices(self):
        vertices = []
        for i in range(6):
            offset = self.calc_vertex_offset(i)
            vertices.append(Point(self.center.x, self.center.y) + offset)
        return vertices

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


def hex_to_pixel(hex):
    x = hex.size * (sqrt(3) * hex.q + sqrt(3) / 2 * hex.r)
    y = hex.size * (3 / 2 * hex.r)
    return Point(x, y)


#   hex_directions = [
#       Hex((1, 0, -1)),  # E
#       Hex((1, -1, 0)),  # NE
#       Hex((0, -1, 1)),  # NW
#       Hex((-1, 0, 1)),  # W
#       Hex((-1, 1, 0)),  # SW
#       Hex((0, 1, -1)),  # SE
#   ]
