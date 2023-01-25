#
# @lc app=leetcode id=909 lang=python3
#
# [909] Snakes and Ladders
#

# @lc code=start
import math
class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        n = len(board)
        min_step = 0
        i, j, curr = n-1, 0, 1
        while curr < n**2:
            # for next_cel in range(curr + 1, min(curr + 6, n**2)):
            i = n - math.ceil(curr/n)
            j = (curr % n) - 1 if i % n else curr % n
            print(curr, f", ({i},{j}),", board[i][j], min_step)
            if board[i][j] != -1:
                min_step += 1
                curr = board[i][j]
            curr +=1
        return min_step


obj = Solution()
board = [[-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1],
         [-1, 35, -1, -1, 13, -1], [-1, -1, -1, -1, -1, -1], [-1, 15, -1, -1, -1, -1]]

print(obj.snakesAndLadders(board))
# @lc code=end
