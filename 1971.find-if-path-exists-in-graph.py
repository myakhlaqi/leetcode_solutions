#
# @lc app=leetcode id=1971 lang=python3
#
# [1971] Find if Path Exists in Graph
#

# @lc code=start
from collections import deque
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        def get_adj(x):
            return { j for i,j in edges if i == x} | {i for i,j in edges if j == x }

        adj = get_adj(source)
        q = deque(adj)
        visited = adj
        while q:
            curr = q.popleft()
            adj = get_adj(curr)
            if curr == destination or destination in adj:
                return True
            adj_notvisited = adj - visited
            if adj_notvisited:
                q.extend(adj_notvisited)
                visited.update(adj_notvisited)
        return False
            
        
# @lc code=end

