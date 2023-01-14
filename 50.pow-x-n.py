#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if x == 0:
            return 0
        def binary_pow(x,n):
            if n == 2:
                return x * x
            if n == 1:
                return x
            result = binary_pow(x * x, n//2)
            return result if n % 2 == 0 else result * x

        result = binary_pow(x,abs(n))
        
        return result if n>0 else 1/result        
# @lc code=end

