from typing import Set, List, Tuple, NewType, Optional, Iterable

Grid = NewType('Grid', List[List[int]])


class Sudoku:
    POSSIBLE_VALUES = set([1, 2, 3, 4, 5, 6, 7, 8, 9])  # Type: Set[int]
    CV = [
        [0, 0, 0, 1, 1, 1, 2, 2, 2],
        [0, 0, 0, 1, 1, 1, 2, 2, 2],
        [0, 0, 0, 1, 1, 1, 2, 2, 2],
        [3, 3, 3, 4, 4, 4, 5, 5, 5],
        [3, 3, 3, 4, 4, 4, 5, 5, 5],
        [3, 3, 3, 4, 4, 4, 5, 5, 5],
        [6, 6, 6, 7, 7, 7, 8, 8, 8],
        [6, 6, 6, 7, 7, 7, 8, 8, 8],
        [6, 6, 6, 7, 7, 7, 8, 8, 8],
    ]

    def __init__(self, grid: Grid) -> None:
        assert len(grid) == 9
        for row in grid:
            assert len(row) == 9

        self._initialise(grid)

    def _initialise(self, grid: Grid) -> None:
        self.grid = grid
        self.row_values = [set(row) - {0} for row in grid]
        self.column_values = [set(col) - {0} for col in self._transpose(grid)]
        self.cell_values = self._get_cell_values()

    def _get_cell_values(self) -> List[Set[int]]:
        cell_values = [set() for _ in self.grid]  # type: List[Set[int]]
        for i, row in enumerate(self.grid):
            for j, elem in enumerate(row):
                if elem != 0:
                    cell_values[self.CV[i][j]].add(elem)
        return cell_values

    @staticmethod
    def _transpose(arr: list):
        return list(zip(*arr))

    def _update_taken_values(self, row: int, col: int, value: int) -> None:
        assert 0 <= row < 9
        assert 0 <= col < 9
        assert 0 < value <= 9

        self.row_values[row].add(value)
        self.column_values[col].add(value)
        self.cell_values[self.CV[row][col]].add(value)

    def _possible_values(self, row: int, col: int) -> Set[int]:
        return \
            self.POSSIBLE_VALUES \
            - self.row_values[row] \
            - self.column_values[col] \
            - self.cell_values[self.CV[row][col]]

    def _refine(self) -> bool:
        changed = False
        for row_i, row in enumerate(self.grid):
            for col_i, elem in enumerate(row):
                if elem == 0:
                    possible_values = self._possible_values(row_i, col_i)
                    if len(possible_values) == 1:
                        value = possible_values.pop()  # there is only one value
                        self.grid[row_i][col_i] = value
                        self._update_taken_values(row_i, col_i, value)
                        changed = True
        return changed

    def is_solved(self) -> bool:
        rows_valid = all([len(set(row)) == 9 for row in self.grid])
        cols_valid = all([len(set(col)) == 9 for col in self._transpose(self.grid)])
        cells_valid = all([len(cell) == 9 for cell in self._get_cell_values()])
        no_zeros = all(elem != 0 for row in self.grid for elem in row)

        return rows_valid and cols_valid and cells_valid and no_zeros

    def _is_solvable(self) -> bool:
        for row_i, row in enumerate(self.grid):
            for col_i, elem in enumerate(row):
                if elem == 0:
                    possible_values = self._possible_values(row_i, col_i)
                    if len(possible_values) == 0:
                        return False
        return True

    def _solve(self) -> Optional[Grid]:
        while self._refine():  # refine while possible. It's cheap and easy
            continue

        if not self._is_solvable():
            return None

        if self.is_solved():  # solved, we are done
            return self.grid

        row, col = self._least_amount_of_work_elem()
        possible_values = self._possible_values(row, col)

        for value in possible_values:
            new_grid = self.copy_grid()
            new_grid[row][col] = value
            sudoku = Sudoku(new_grid)
            solved_grid = sudoku._solve()
            if solved_grid is not None:
                return solved_grid

        return None

    def solve(self) -> None:
        solved_grid = self._solve()
        if solved_grid is not None:
            self._initialise(solved_grid)

    def _least_amount_of_work_elem(self) -> Tuple[int, int]:
        least_values = 10
        r, c = (-1, -1)
        for row_i, row in enumerate(self.grid):
            for col_i, elem in enumerate(row):
                possible_values = self._possible_values(row_i, col_i)
                if elem == 0 and len(possible_values) < least_values:
                    # return row_i, col_i
                    least_values = len(possible_values)
                    r = row_i
                    c = col_i

        assert 0 <= r < 9
        assert 0 <= c < 9

        return (r, c)

    def copy_grid(self) -> Grid:
        new_grid = [[elem for elem in row] for row in self.grid]
        return Grid(new_grid)

    @staticmethod
    def chunks(l: Iterable, chunk_size: int):
        for i in range(0, len(l), chunk_size):
            yield l[i: i + chunk_size]

    def __str__(self) -> str:
        HS = "|"  # Horizontal separator
        VS = "-"  # Vertical separator
        IN = "+"  # Intersection
        divider_row = IN + 3 * (5 * VS + IN)

        def n_to_str(n: int) -> str:
            if n == 0:
                return " "
            else:
                return str(n)

        rows = [divider_row]
        for row_chunk in self.chunks(self.grid, 3):
            for row in row_chunk:
                chunks = self.chunks(row, 3)
                chunks = [" ".join(map(n_to_str, chunk)) for chunk in chunks]
                rows.append(HS + HS.join(chunks) + HS)
            rows.append(divider_row)

        return "\n".join(rows)
