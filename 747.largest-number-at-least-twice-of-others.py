#
# @lc app=leetcode id=747 lang=python3
#
# [747] Largest Number At Least Twice of Others
#

# @lc code=start
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_ix=0
        for i in range(len(nums)):
            if nums[i] > nums[max_ix]:
                max_ix=i
        # print([nums[max_ix] >= 2*x  for x in nums if x!=nums[max_ix] ])
        return max_ix if all(nums[max_ix] >= 2*x  for x in nums if x!=nums[max_ix] ) else -1
# @lc code=end

