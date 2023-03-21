#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # return math.sqrt(num) == int(math.sqrt(num))
        left = 1
        right = num
        while left<=right:
            mid = (left +right)//2
            if mid * mid == num:
                return True
            elif mid * mid < num:
                left = mid + 1
            else:
                right = mid - 1
        return False        
# @lc code=end

