#
# @lc app=leetcode id=154 lang=python3
#
# [154] Find Minimum in Rotated Sorted Array II
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l<r:
            mid = (l+r)//2
            if  nums[l] == nums[mid] == nums[r]:
                return min(nums)
            if nums[mid]> nums[mid+1]:
                return nums[mid+1]
            elif nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid
        
        return nums[0] if l == len(nums) - 1 else nums[l]
                    
# @lc code=end

