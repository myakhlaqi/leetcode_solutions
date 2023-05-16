#
# @lc app=leetcode id=658 lang=python3
#
# [658] Find K Closest Elements
#

# @lc code=start
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        r = len(arr) - 1
        while l<= r:
            mid = (l+r) // 2
            if arr[mid] == x:
                l = mid
                break
            elif arr[mid] < x:
                l = mid + 1
            else:
                r = mid - 1
        ix = l if l < len(arr) - 1 else len(arr) - 1
        l,r = ix-1 , ix
        counter = 0
        while counter < k:
            if l < 0:
                r += 1
            elif r > len(arr) - 1:
                l -= 1
            else:
                if abs(arr[l] -  x) <=  abs(arr[r] -  x):
                    l -= 1
                else:
                    r += 1
            counter += 1
        return arr[l+1 : r]
                
                
                    
# @lc code=end

