#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
# @lc code=start

class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index=dict()
        for i in range(len(nums)):
            if nums[i] in num_index:
                num_index[nums[i]].append(i)
            else:
                num_index[nums[i]]=[i]
                
        for i in nums:
            complement = target - i
            if complement == i and len(num_index[i])>1:
                return num_index[i]
            if complement != i and complement in num_index:
                return [num_index[i][0],num_index[target-i][0]]        
            
# @lc code=end

