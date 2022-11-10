#
# @lc app=leetcode id=1991 lang=python3
#
# [1991] Find the Middle Index in Array
#

# @lc code=start

class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total_sum= sum(nums)
        left_sum=right_sum=0
        for i,item in enumerate(nums):
            right_sum=total_sum-left_sum-item
            if right_sum == left_sum:
                return i
            left_sum+=item
        return -1
            
        
# @lc code=end

