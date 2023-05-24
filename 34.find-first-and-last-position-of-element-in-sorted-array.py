#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        l = 0
        r = len(nums) - 1
        while l<r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] == target:
                r = mid 
            else:
                r = mid - 1
        
        if nums[l] != target:
            return [-1,-1]
        else:
            
            end = start = l
            r = len(nums) - 1
            while l<=r:
                
                mid = (l +r) // 2
                if nums[mid] == target:
                    l = mid + 1
                else:
                    r = mid - 1
            end = r        
            return [start,end]
                    
# @lc code=end

