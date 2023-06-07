#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        i, j , k = 0 , 0, 0
        if len(nums1) < len(nums2):
            nums1 , nums2 = nums2 , nums1
        total = len(nums1) + len(nums2)
        half = total // 2
        while i < len(nums1):
            print(i,j,k)
            if j == len(nums2) or nums1[i] <= nums2[j]: 
                i+=1
            else: 
                j+=1
            k+=1
            if k==half:
                break
        
        return   min(nums1[i],nums2[j]) if total % 2 else (max(nums1[i-1],nums2[j-1]),min(nums1[i],nums2[j])) /2        
        
# @lc code=end

