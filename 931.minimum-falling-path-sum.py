#
# @lc app=leetcode id=931 lang=python3
#
# [931] Minimum Falling Path Sum
#

# @lc code=start
import itertools
from collections import deque


class Solution:
    # def minFallingPathSum(self, M: List[List[int]]) -> int:
    #     n = len(M)
    #     for i, j in itertools.product(range(1, n), range(n)):
    #         if j == 0:
    #             M[i][j] += min(M[i-1][j], M[i-1][j+1])
    #         elif j == n - 1:
    #             M[i][j] += min(M[i-1][j], M[i-1][j-1])
    #         else:
    #             M[i][j] += min(M[i-1][j], M[i-1][j+1], M[i-1][j-1])

    #     return min(M[n-1])

    # BFS solution
    # def minFallingPathSum(self, matrix: List[List[int]]) -> int:
    #     m = len(matrix)
    #     n = len(matrix[0])
    #     visited = {}
    #     for j in range(n):
    #         queue = deque([(0, j)])
    #         visited[(0, j)] = matrix[0][j]
    #         while queue:
    #             i, j = queue.popleft()
    #             for x, y in [(i+1, j), (i+1, j+1), (i+1, j-1)]:
    #                 if x < m and 0 <= y < n:
    #                     queue.append((x, y))
    #                     if (x, y) not in visited:
    #                         visited[(x, y)] = visited[(i, j)] + matrix[x][y]
    #                     else:
    #                         visited[(x, y)] = min(visited[(x, y)],
    #                                               visited[(i, j)] + matrix[x][y])

    #     return min(visited[( m - 1, j)] for j in range(n))

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        min_sum = sys.maxsize
        
        def helper(matrix, i, j, sum):
            if i == len(matrix):
                return sum
            if j < 0 or j >= len(matrix[0]) or i > len(matrix):
                return sys.maxsize

            sum1 = helper(matrix, i+1, j, sum + matrix[i][j])
            sum2 = helper(matrix, i+1, j-1, sum + matrix[i][j])
            sum3 = helper(matrix, i+1, j+1, sum + matrix[i][j])


            return min(sum1, sum2, sum3)

        for j in range(len(matrix[0])):
            min_sum = min( min_sum ,helper(matrix, 0, j, 0))

        return min_sum
# @lc code=end
