"""  Valid Sudoku """

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        vert = list(map(list, zip(*board)))
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in board[i][j+1:] or board[i][j] in board[i][:j]:
                    return False
                if board[i][j] in vert[j][i+1:] or board[i][j] in vert[j][:i]:
                    return False
                w = int(i/3)
                h = int(j/3)
                if i%3 == 0:
                    if board[i][j] in board[i+1][h*3:(h+1)*3] or board[i][j] in board[i+2][h*3:(h+1)*3]:
                        return False
                elif i%3 == 1:
                    if board[i][j] in board[i-1][h*3:(h+1)*3] or board[i][j] in board[i+1][h*3:(h+1)*3]:
                        return False
                elif i%3 == 2:
                    if board[i][j] in board[i-1][h*3:(h+1)*3] or board[i][j] in board[i-2][h*3:(h+1)*3]:
                        return False
        return True

s = Solution()
print (s.isValidSudoku([[".","8","7","6","5","4","3","2","1"],["2",".",".",".",".",".",".",".","."],["3",".",".",".",".",".",".",".","."],["4",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".",".","."],["6",".",".",".",".",".",".",".","."],["7",".",".",".",".",".",".",".","."],["8",".",".",".",".",".",".",".","."],["9",".",".",".",".",".",".",".","."]]))