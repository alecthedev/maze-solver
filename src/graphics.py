from tkinter import BOTH, Canvas, Tk


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x, self.y = x, y


class Line:
    def __init__(self, start: Point, end: Point):
        self.start, self.end = start, end

    def draw(self, canvas: Canvas, fill_color: str):
        canvas.create_line(
            self.start.x, self.start.y, self.end.x, self.end.x, fill=fill_color, width=2
        )


class Window:
    def __init__(self, width: int, height: int) -> None:
        self._root = Tk()
        self._root.title("Maze Solver")
        self._canvas = Canvas(self._root, width=width, height=height)
        self._canvas.pack()
        self._running = False
        self._root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self._canvas.update_idletasks()
        self._canvas.update()

    def wait_for_close(self):
        self._running = True
        while self._running:
            self.redraw()

    def close(self):
        self._running = False

    def draw_line(self, line: Line, fill_color: str):
        line.draw(self._canvas, fill_color)
