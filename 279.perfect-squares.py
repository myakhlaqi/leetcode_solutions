#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#

# @lc code=start
from collections import deque
from math import sqrt
class Solution:
    def numSquares(self, n: int) -> int:
        if n == int(sqrt(n)) ** 2:
            return 1
        step = int(sqrt(n))
        q = deque([n])
        visited = {n}
        ans = 0
        while q:
            size = len(q)
            for _ in range(size):
                curr = q.popleft()
                for i in range(1,step+1):
                    diff = curr - (i ** 2)
                    if diff == 0:
                        return ans + 1
                    if diff > 0 and diff not in visited:
                        visited.add(diff)
                        q.append(diff)
            ans +=1
        return ans
            
# @lc code=end

