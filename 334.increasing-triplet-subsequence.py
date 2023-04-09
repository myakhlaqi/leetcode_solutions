#
# @lc app=leetcode id=334 lang=python3
#
# [334] Increasing Triplet Subsequence
#

# @lc code=start
import sys
class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        
        first, second = inf, inf
        
        for third in nums:
            
            if second < third: return True
            if third <= first: first = third    
            else:  second = third 
                
        return  False

# class Solution:
#     def increasingTriplet(self, nums) -> bool:
#         uniq=set(nums)
#         if len(uniq) < 3:
#             return False
        
#         last_min = sys.maxsize
#         n = len(nums)
#         for i in range(n):
#             if nums[i] < last_min:
#                 curr_max = nums[i]
#                 counter = 1
#                 for j in range(i+ 1, n):
#                     if nums[j] > nums[i]:
#                         # print(i, j, curr_max, nums[j], counter)
#                         if nums[j] > curr_max:
#                             counter += 1
#                         curr_max = nums[j]
#                     if counter == 3:
#                             return True
#                 last_min = min(last_min, nums[i])

#         return False


obj = Solution()
# print(obj.increasingTriplet([1,5,0,4,1,3]))
# print(obj.increasingTriplet([2, 1, 5, 0, 3]))
print(obj.increasingTriplet([20,100,10,12,5,13]))


# @lc code=end
