#
# @lc app=leetcode id=2099 lang=python3
#
# [2099] Find Subsequence of Length K With the Largest Sum
#

# @lc code=start
import heapq
class Solution:
    def maxSubsequence(self, nums: list[int], k: int) -> list[int]:
        klarg = [] 
        for i,v in enumerate(nums):
            if len(klarg) == k:
                heapq.heappushpop(klarg,(v,i) )
            else:
                heapq.heappush(klarg,(v,i) )
        return list(map(lambda x: x[0], sorted(klarg,key= lambda x: x[1])))
        
    
    # def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
    #     ans = list(enumerate(nums))
    #     ans = sorted(ans,key= lambda x: x[1])[-k:]
    #     ans.sort(key= lambda x: x[0])
    #     return list(map(lambda x:x[1],ans))        
        
# @lc code=end

