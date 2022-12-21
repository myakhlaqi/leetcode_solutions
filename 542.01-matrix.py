#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#

# @lc code=start
from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        q = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i,j))
                else:
                    mat[i][j] = sys.maxsize

        while q:
            i,j = q.popleft()
            neighbors = set((x,y) for x,y in [(i+1,j),(i-1,j),(i,j-1),(i,j+1)]
                             if 0 <= x<m and 0<= y < n )

            for r,c in neighbors:
                if mat[r][c] > mat[i][j] + 1:
                    mat[r][c] = mat[i][j] + 1
                    q.append((r,c))
        return mat        
# obj = Solution()
# A = [[0,0,0],[0,1,0],[1,1,1]]
# obj.updateMatrix(A)
# @lc code=end

