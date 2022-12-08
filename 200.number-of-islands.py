#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
import itertools
from collections import deque

class Solution:
    def BFS(self, grid, start):
        queue = deque([start])
        visited = {start}
        while queue:
            i, j = queue.popleft()
            if neighbors := [(x, y) for x, y in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)] if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == "1" and (x, y) not in visited]:
                queue.extend(neighbors)
                visited.update(neighbors)
        return visited

    def numIslands(self, grid) -> int:
        n = len(grid)
        m = len(grid[0])
        islands = 0
        visited = set()
        for i, j in itertools.product(range(n), range(m)):
            if grid[i][j] == "1" and (i, j) not in visited:
                visited.update(self.BFS(grid, (i, j)))
                islands += 1
        return islands


# @lc code=end
