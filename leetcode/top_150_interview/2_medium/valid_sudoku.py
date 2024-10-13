"""
Type: Medium
36. Valid Sudoku
https://leetcode.com/problems/valid-sudoku/description/?envType=study-plan-v2&envId=top-interview-150
"""

from icecream import ic
from typing import List

from collections import defaultdict


class Solution:
    @staticmethod
    def isValidSudoku(board: List[List[str]]) -> bool:
        def box_translator(row, cell):
            if row < 3 and cell < 3:
                return "0"
            elif row < 3 and cell < 6:
                return "1"
            elif row < 3 and cell < 9:
                return "2"
            elif row < 6 and cell < 3:
                return "3"
            elif row < 6 and cell < 6:
                return "4"
            elif row < 6 and cell < 9:
                return "5"
            elif row < 9 and cell < 3:
                return "6"
            elif row < 9 and cell < 6:
                return "7"
            elif row < 9 and cell < 9:
                return "8"

        row_i = 0
        cell_i = 0
        row_counter = defaultdict(set)
        column_counter = defaultdict(set)
        box_counter = defaultdict(set)

        for row in board:
            for cell in row:
                box = box_translator(row_i, cell_i)
                if cell != ".":
                    if (cell in box_counter[box]
                            or cell in row_counter[str(row_i)]
                            or cell in column_counter[str(cell_i)]):
                        return False
                    else:
                        box_counter[box].add(cell)
                        row_counter[str(row_i)].add(cell)
                        column_counter[str(cell_i)].add(cell)
                cell_i += 1
            row_i += 1
            cell_i = 0
        return True


import unittest


class SolutionTest(unittest.TestCase):

    def test_solution(self):
        test_cases = [
            ([["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]], True),

            ([["8","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]], False)
        ]

        for board, expected_output in test_cases:

            self.assertEqual(expected_output, Solution.isValidSudoku(board=board))


if __name__ == '__main__':
    unittest.main()