#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
import sys
class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        nums.sort()
        n= len(nums)
        
        min_sum=sys.maxsize
        for i in range(n-2):
            start,end= i+1,n-1
            while start < end:
                curr_sum= nums[i] + nums[start] + nums[end]
                if(curr_sum>target):
                    end-=1
                elif curr_sum<target:
                    start+=1
                else:
                    return curr_sum
                if abs(curr_sum-target)<abs(min_sum-target):
                    min_sum=curr_sum
        
        return min_sum
obj= Solution()
print(obj.threeSumClosest([-1,2,1,-4],1))
# @lc code=end

