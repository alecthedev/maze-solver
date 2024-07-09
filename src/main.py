from graphics import Line, Point, Window
from hex import Hex
from maze import Maze

WIDTH, HEIGHT = 800, 800
CENTER = Point(WIDTH // 2, HEIGHT // 2)


def main():
    window = Window(WIDTH, HEIGHT)

    maze = Maze(CENTER, 25, 4, window, seed=100)

    window.wait_for_close()


main()
