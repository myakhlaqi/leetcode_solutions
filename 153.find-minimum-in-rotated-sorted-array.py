#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l<r:
            mid = (l+r) //2
            # print(l,mid,r)
            if nums[l]<nums[mid]<nums[r]:
                return nums[0]
            if nums[mid]>nums[mid+1]:
                return nums[mid+1]
            elif nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        return nums[l]
                    
# @lc code=end

