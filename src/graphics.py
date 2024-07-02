from tkinter import BOTH, Canvas, Tk


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
