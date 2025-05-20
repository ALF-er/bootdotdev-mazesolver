from tkinter import Tk, Canvas

class Window():
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title = "Maze Solver"
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        self.__canvas = Canvas(width=width, height=height)
        self.__canvas.pack()

        self.__running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False

    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)

    def draw_cell(self, cell):
        cell.draw(self.__canvas)

    def draw_move(self, from_cell, to_cell, undo=False):
        from_cell.draw_move(self.__canvas, to_cell, undo)

    def draw_maze(self, maze):
        maze.draw(self.__canvas)
