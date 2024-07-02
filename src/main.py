import graphics as g


def main():
    window = g.Window(800, 600)
    p1 = g.Point(50, 100)
    p2 = g.Point(200, 450)
    window.draw_line(g.Line(p1, p2), "black")
    window.draw_line(g.Line(g.Point(0, 0), g.Point(511, 64)), "red")
    window.wait_for_close()


main()
