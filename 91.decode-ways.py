#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
from collections import deque
class Solution:
    def numDecodings(self, s: str) -> int:
        self.memo = {}
        return self.helper(s)

    def helper(self, s: str) -> int:
        if len(s) == 0: return 1
        if s in self.memo: return self.memo[s]
        
        takeOne = takeTwo = 0
        
        if int(s[:1]) >= 1 and int(s[:1]) <= 9:
            takeOne = self.helper(s[1:])
        
        if int(s[:2]) >= 10 and int(s[:2]) <= 26: 
            takeTwo = self.helper(s[2:])
        
        self.memo[s] = takeOne + takeTwo
        
        return self.memo[s]


# class Solution:
#     def numDecodings(self, s: str) -> int:
#         start = ""

#         def decode(substr):
#             if len(substr) == len(s):
#                 return 1
#             result = 0
#             if len(substr) < len(s) and   1 <= int(s[len(substr)]) < 10 :
#                 result += decode(s[:len(substr)+1])
#             if len(substr) < len(s) -1 and  10 <= int(s[len(substr):len(substr)+2]) < 27 :
#                 result += decode(s[:len(substr)+2])

#             return result
        
#         return decode(start)

    # BFS solution
    # def numDecodings(self, s: str) -> int:
    #     # if len(set(s)) == 1:
    #     #     return 2 ** len(s) - 1
    #     valid_set = {str(x) for x in range(1,27)}
    #     # print(valid_set)
    #     q = deque([0])
    #     ans = 0
    #     while q:
    #         # print(q,end=", ")
    #         curr = q.popleft()
    #         # print(curr,end="\n")

    #         if curr < len(s) and s[curr:][0] in valid_set :
    #             if curr + 1 == len(s):
    #                 ans +=1
    #             else:
    #                 q.append(curr + 1)
    #         if curr < len(s) - 1 and s[curr:][0:2] in valid_set:
    #             if curr + 2 == len(s):
    #                 ans += 1
    #             else:
    #                 q.append(curr + 2)
                
    #     return ans        
# @lc code=end

