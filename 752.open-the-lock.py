#
# @lc app=leetcode id=752 lang=python3
#
# [752] Open the Lock
#

# @lc code=start
from collections import deque

class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        deadends = set(deadends)
        if "0000" in deadends:
            return -1
        if target == "0000":
            return 0
        q = deque(["0000"])
        visited= {"0000"}
        ans = 0
        while q:
            size = len(q)
            for _ in range(size):
                curr = q.popleft()
                for i in range(len(curr)):
                    up_num = curr[:i]+ str( (int(curr[i])+1) % 10 ) + curr[i+1:]
                    down_num = curr[:i]+ str( (int(curr[i])-1) % 10 ) + curr[i+1:]
                    # print(curr,up_num,down_num,ans)
                    if up_num not in visited and up_num not in deadends:
                        if up_num == target:
                            return ans + 1
                        visited.add(up_num)
                        q.append(up_num)
                    if down_num not in visited and down_num not in deadends:
                        if down_num == target:
                            return ans + 1
                        visited.add(down_num)
                        q.append(down_num)
            ans += 1
        return -1
# @lc code=end    
                
        
# @lc code=end

