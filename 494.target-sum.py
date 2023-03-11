#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#

# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.memory= dict()
        # bottom-up approach
        def helper(nums,i,s, target):
            if i == len(nums):
                if s == target:
                    return 1 # One is found
                return 0 # not found
            # if have the answer for the current path return the result
            if (i,s) in self.memory: 
                return self.memory[(i,s)]
            find1= helper(nums,i+1,s, target)
            find2= helper(nums ,i+1 , s - 2*nums[i] , target)
            
            # memorize the answer for the current path
            self.memory[(i,s)] = find1 + find2
            return self.memory[(i,s)]
            
        return helper(nums, 0 , sum(nums), target )
    
        
# @lc code=end

