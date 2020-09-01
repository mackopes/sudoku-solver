import pprint as pprint_module

from sudoku import Sudoku
from example_inputs.example_sudoku import *

pprint = pprint_module.PrettyPrinter(indent=4).pprint


def main():
    sudoku = Sudoku(example_sudoku_expert)
    print(sudoku)

    sudoku.solve()

    print(sudoku.is_solved())
    print(sudoku)


if __name__ == "__main__":
    main()
