#
# @lc app=leetcode id=334 lang=python3
#
# [334] Increasing Triplet Subsequence
#

# @lc code=start
import sys
class Solution:
    def increasingTriplet(self, nums) -> bool:
        last_min=sys.maxsize
        n = len(nums)
        for i in range(n):
            if nums[i]<last_min:
                curr_max=nums[i]
                counter=0
                for j in range(i+1,n):
                    if nums[j]> curr_max:
                        curr_max=nums[j]
                        counter+=1
                    if counter==3:
                        return True
                last_min= min(last_min,curr_max)
        
        return False
            
                
                    
                        
# @lc code=end

