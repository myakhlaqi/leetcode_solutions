#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_dic={}
        for ix,val in enumerate(nums):
            if val not in num_dic:
                num_dic[val] = (ix,sys.maxsize)
            else:
                num_dic[val] = (ix,min(abs(num_dic[val][0] - ix),num_dic[val][1]))
                if num_dic[val][1] <=k:
                    return True
        
        return False      
# @lc code=end

