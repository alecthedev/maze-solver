from graphics import Point, Window
from maze import Maze

WIDTH, HEIGHT = 800, 800
CENTER = Point(WIDTH // 2, HEIGHT // 2)


def main():
    window = Window(WIDTH, HEIGHT)

    maze = Maze(CENTER, 15, 10, window)
    maze.solve()

    window.wait_for_close()


main()
