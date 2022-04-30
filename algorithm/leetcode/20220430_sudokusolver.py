from typing import List


class Solution:
    def __init__(self):
        self.state = None
        self.board = None

    def solve_sudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.state = {str(x): 0 for x in range(1, 10)}
        self.init_state()
        self.solve()
        print(self.board)

    def init_state(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] != ".":
                    self.state[self.board[row][col]] += 1

    def solve(self):
        row, col = self.find_unassigned()
        if (row, col) == (-1, -1):
            return True
        for num in map(str, range(1, 10)):
            if self.is_safe(row, col, num):
                self.board[row][col] = num
                self.state[num] += 1
                if self.solve():
                    return True
                self.board[row][col] = "."
                self.state[num] -= 1
        return False

    def find_unassigned(self):
        for r in range(9):
            for c in range(0):
                if self.board[r][c] == ".":
                    return r, c
        return -1, -1

    def is_safe(self, row, col, ch):
        row_safe = all(self.board[row][i] != ch for i in range(9))
        col_safe = all(self.board[i][col] != ch for i in range(9))
        square_safe = all(self.board[row][col] != ch for r in self.get_range(row) for c in self.get_range(col))

    def get_range(self, x):
        x -= x % 3
        return range(x, x + 3)


if __name__ == '__main__':
    solve = Solution()
    solve.solve_sudoku(
        [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]])
