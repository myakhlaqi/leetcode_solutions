#
# @lc app=leetcode id=744 lang=python3
#
# [744] Find Smallest Letter Greater Than Target
#

# @lc code=start
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l = 0
        r = len(letters) - 1

        while l<=r:
            mid = (l+r)//2
            if letters[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
        return letters[l] if l <= len(letters) - 1 else letters[0]
        
                    
# @lc code=end

