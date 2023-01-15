#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

# @lc code=start

# https://leetcode.com/problems/find-peak-element/solutions/2963688/3-solutions-binary-search-monotonic-stack-brute-force/

class Solution:
    # binary search O(log n) time and O(log n) space
    def findPeakElement(self, nums: List[int]) -> int:
        def binary_search(nums,l,r):
            if l+1 >= r:
                return l if nums[l] > nums[r] else r
            mid=(l+r)//2
            left_peak_ix = binary_search(nums,l,mid)
            right_peak_ix = binary_search(nums,mid+1,r)
            
            return left_peak_ix if nums[left_peak_ix] > nums[right_peak_ix] else right_peak_ix
        
        return binary_search(nums,0,len(nums) - 1)
        
    
    # monotonic stack O(n) time and O(1) space
#     def findPeakElement(self, nums: List[int]) -> int:
#         peak = [0]
#         for ix,val in enumerate(nums):
#             if val > nums[peak[-1]]:
#                 peak.pop()
#                 peak.append(ix)
#         return peak[-1]
    
#     # brute force O(n) time and O(1) space
#     def findPeakElement(self, nums: List[int]) -> int:
#         max_val = max(nums)
#         return [ix for ix , v in enumerate(nums) if v == max_val][0]        
# @lc code=end

