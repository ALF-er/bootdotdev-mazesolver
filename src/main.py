from window import Window
from point import Point
from maze import Maze

def main():
    win = Window(800, 600)

    # cell1 = Cell(Point(10, 10), Point(110, 110))
    # cell2 = Cell(Point(111, 10), Point(211, 110), True, True, False, False)
    # cell3 = Cell(Point(10, 111), Point(110, 211), False, False, True, True)
    # cell4 = Cell(Point(111, 111), Point(211, 211), True, False, True, False)
    #
    # win.draw_cell(cell1)
    # win.draw_cell(cell2)
    # win.draw_cell(cell3)
    # win.draw_cell(cell4)
    #
    # win.draw_move(cell1, cell2)
    # win.draw_move(cell2, cell4, True)
    # win.draw_move(cell4, cell3, True)
    # win.draw_move(cell1, cell4)

    maze = Maze(Point(5, 5), 20, 30, 25, 25)
    win.draw_maze(maze)
    maze.solve()

    win.wait_for_close()

main()
