import itertools

class Solution:
    
    def isValidSudoku(self, board):
        for i in range(9):
            seen=set()
            for j in range(9):
                if board[i][j]!=".":
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])
                    
        for i in range(9):
            seen=set()
            for j in range(9):
                if board[j][i]!=".":
                    if board[j][i] in seen:
                        return False
                    seen.add(board[j][i])

        for i, j in itertools.product(range(3), range(3)):
            seen=set()
            for k, l in itertools.product(range(3*j,3*j+3), range(3*i,3*i+3)):
                if board[k][l]!=".":
                    if board[k][l] in seen:
                        return False
                    seen.add(board[k][l])
        return True



# @lc code=end

