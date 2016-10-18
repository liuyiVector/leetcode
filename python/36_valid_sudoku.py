#! usr/bin/python
# coding=utf-8 //这句是使用utf8编码方式方法,可以单独加入python头使用
# A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.

class Solution(object):
    def isValidList(self, arrs):
        arrs = filter(lambda x : x != '.', arrs)
        return len(set(arrs)) == len(arrs)
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(0,9):
            if not self.isValidList([board[i][j] for j in range(0,9)]) or \
                not self.isValidList([board[j][i] for j in range(0,9)]):
                return False
        for i in range(0,3):
            for j in range(0,3):
                if not self.isValidList([board[m][n] for n in range(3*j, 3*j + 3) \
                    for m in range(3*i, 3*i + 3)]):
                    return False
        return True



if __name__ == '__main__':
    board = [[1, '.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', 2, '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', 3, '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', 4, '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', 5, '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', 6, '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', 7, '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', 8, '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.', 9]]
    print Solution().isValidSudoku(board)
