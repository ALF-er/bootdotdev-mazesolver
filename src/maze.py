import random

from point import Point
from cell import Cell

class Maze():
    def __init__(
        self,
        position,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        seed=None,
    ):
        self.position = position
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.cells = []
        self.create_cells()
        self.__break_entrance_and_exit()
        if seed is not None:
            random.seed(seed)
        self.__break_walls_r(0, 0)
        self.__reset_cells_visited()

    def create_cells(self):
        self.cells = []
        for i in range(self.num_cols):
            self.cells.append([])

            for j in range(self.num_rows):
                self.cells[i].append(
                    Cell(
                        Point(self.position.x + self.cell_size_x * i, self.position.y + self.cell_size_y * j),
                        Point(self.position.x + self.cell_size_x * (i + 1), self.position.y + self.cell_size_y * (j + 1)),
                    )
                )

    def draw(self, canvas):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self.cells[i][j].draw(canvas)

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self.cells[i][j].visited = True

        if i == len(self.cells) - 1 and j == len(self.cells[i]) - 1:
            return True

        if j > 0 and not self.cells[i][j].has_top_wall and not self.cells[i][j - 1].visited:
            if self._solve_r(i, j - 1):
                return True

        if i < len(self.cells) - 1 and not self.cells[i][j].has_right_wall and not self.cells[i + 1][j].visited:
            if self._solve_r(i + 1, j):
                return True

        if j < len(self.cells[i]) - 1 and not self.cells[i][j].has_bottom_wall and not self.cells[i][j + 1].visited:
            if self._solve_r(i, j + 1):
                return True

        if i > 0 and not self.cells[i][j].has_left_wall and not self.cells[i - 1][j].visited:
            if self._solve_r(i - 1, j):
                return True

        return False

    def __break_entrance_and_exit(self):
        if len(self.cells) > 0:
            self.cells[0][0].has_top_wall = False
            self.cells[-1][-1].has_bottom_wall = False

    def __break_walls_r(self, i, j):
        self.cells[i][j].visited = True
        while True:
            possible_directions = []

            if j > 0 and not self.cells[i][j - 1].visited:
                possible_directions.append("top")
            if i < len(self.cells) - 1 and not self.cells[i + 1][j].visited:
                possible_directions.append("right")
            if j < len(self.cells[i]) - 1 and not self.cells[i][j + 1].visited:
                possible_directions.append("bottom")
            if i > 0 and not self.cells[i - 1][j].visited:
                possible_directions.append("left")

            if len(possible_directions) == 0:
                return

            direction = random.choice(possible_directions)

            match direction:
                case "top":
                    self.cells[i][j].has_top_wall = False
                    self.cells[i][j - 1].has_bottom_wall = False
                    self.__break_walls_r(i, j - 1)
                case "right":
                    self.cells[i][j].has_right_wall = False
                    self.cells[i + 1][j].has_left_wall = False
                    self.__break_walls_r(i + 1, j)
                case "bottom":
                    self.cells[i][j].has_bottom_wall = False
                    self.cells[i][j + 1].has_top_wall = False
                    self.__break_walls_r(i, j + 1)
                case "left":
                    self.cells[i][j].has_left_wall = False
                    self.cells[i - 1][j].has_right_wall = False
                    self.__break_walls_r(i - 1, j)

    def __reset_cells_visited(self):
        for col in self.cells:
            for cell in col:
                cell.visited = False
