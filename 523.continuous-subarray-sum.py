#
# @lc app=leetcode id=523 lang=python3
#
# [523] Continuous Subarray Sum
#
# @lc code=start

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n= len(nums)
        i=0
        prefix_sum = [0]*(n+1)
        for i in range(n):
            prefix_sum[i+1]=prefix_sum[i]+nums[i]
        # print(prefix_sum)
        for i in range(2,n+1):
            j=0
            while j+i<= n:
                # sum_=(nums[j:j+i])
                sum_= prefix_sum[j+i]-prefix_sum[j]
                # print(nums[j:j+i],sum_)
                if (sum_ >= k and sum_ % k == 0) or (sum_ == 0):
                    return True
                j+=1   
                 
            i+=1
        return False

      
# @lc code=end

