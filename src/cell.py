class Cell():
    def __init__(self, point1, point2, has_top_wall=True, has_right_wall=True, has_bottom_wall=True, has_left_wall=True):
        self.has_top_wall = has_top_wall
        self.has_right_wall = has_right_wall
        self.has_bottom_wall = has_bottom_wall
        self.has_left_wall = has_left_wall
        self.__point1 = point1
        self.__point2 = point2
        self.visited = False

    def draw(self, canvas):
        canvas.create_line(
            self.__point1.x,
            self.__point1.y,
            self.__point2.x,
            self.__point1.y,
            fill=("black" if self.has_top_wall else "#d9d9d9"),
            width=2
        )
        canvas.create_line(
            self.__point2.x,
            self.__point1.y,
            self.__point2.x,
            self.__point2.y,
            fill=("black" if self.has_right_wall else "#d9d9d9"),
            width=2
        )
        canvas.create_line(
            self.__point1.x,
            self.__point2.y,
            self.__point2.x,
            self.__point2.y,
            fill=("black" if self.has_bottom_wall else "#d9d9d9"),
            width=2
        )
        canvas.create_line(
            self.__point1.x,
            self.__point1.y,
            self.__point1.x,
            self.__point2.y,
            fill=("black" if self.has_left_wall else "#d9d9d9"),
            width=2
        )

    def draw_move(self, canvas, to_cell, undo=False):
        canvas.create_line(
            self.__point1.x + (self.__point2.x - self.__point1.x) * 0.5,
            self.__point1.y + (self.__point2.y - self.__point1.y) * 0.5,
            to_cell.__point1.x + (to_cell.__point2.x - to_cell.__point1.x) * 0.5,
            to_cell.__point1.y + (to_cell.__point2.y - to_cell.__point1.y) * 0.5,
            fill=("grey" if undo else "red"),
            width=2
        )
