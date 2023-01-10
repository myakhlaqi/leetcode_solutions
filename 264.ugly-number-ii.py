#
# @lc app=leetcode id=264 lang=python3
#
# [264] Ugly Number II
#

# @lc code=start
class Solution:
    
    def nthUglyNumber(self, n: int) -> int:
        prime_factors = [2,3,5]
        ans = []
        i = 1
        while len(ans) < n:
            j,tmp = i , i
            for factor in prime_factors:
                while j % factor == 0:
                    j  = j//factor
            if j == 1:
                ans.append(tmp)
            i+=1
        # print(ans)
        return ans[-1]
        
# @lc code=end

