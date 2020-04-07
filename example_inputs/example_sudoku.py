from sudoku import Grid

example_sudoku_evil = Grid([
    [2, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 6, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 6]
])

example_sudoku_easy = Grid([
    [7, 3, 0, 9, 5, 0, 0, 0, 0],
    [2, 0, 0, 6, 7, 0, 5, 8, 0],
    [0, 0, 5, 0, 1, 0, 4, 0, 0],
    [1, 9, 0, 0, 6, 3, 2, 0, 5],
    [0, 4, 0, 0, 0, 0, 6, 0, 0],
    [5, 6, 8, 2, 0, 7, 0, 0, 0],
    [0, 2, 0, 0, 8, 1, 3, 0, 0],
    [0, 0, 1, 0, 0, 9, 7, 6, 0],
    [0, 7, 0, 5, 2, 0, 8, 0, 9]
])

example_sudoku_hard = Grid([
    [0, 5, 1, 0, 0, 0, 0, 0, 0],
    [2, 0, 0, 7, 0, 0, 0, 0, 5],
    [0, 0, 0, 4, 0, 0, 9, 6, 0],
    [0, 0, 2, 0, 5, 7, 4, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 5, 3],
    [0, 7, 5, 0, 9, 0, 0, 0, 0],
    [8, 0, 4, 6, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 3, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 8, 2, 7]
])

example_sudoku_expert = Grid([
    [5, 0, 0, 0, 0, 7, 0, 1, 0],
    [0, 4, 0, 0, 0, 0, 0, 0, 0],
    [1, 9, 0, 0, 0, 0, 0, 0, 0],
    [9, 0, 0, 0, 0, 0, 0, 4, 5],
    [0, 0, 0, 3, 0, 9, 0, 0, 6],
    [4, 0, 3, 0, 0, 6, 0, 0, 0],
    [7, 3, 0, 5, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 7, 9],
    [0, 1, 0, 0, 6, 0, 0, 0, 0]
])
