#
# @lc app=leetcode id=1239 lang=python3
#
# [1239] Maximum Length of a Concatenated String with Unique Characters
#

# @lc code=start
class Solution:
    def maxLength(self, arr) -> int:
        n = len(arr)
        max_len=len(arr[0])
        for i in range(n):
            if len(arr[i]) != len(set(arr[i]) ):
                arr[i]=None
        print(arr)
        for i in range(n-1):
            if arr[i] is not None:
                max_curr=len(arr[i])
                for j in range(i+1,n):
                    if arr[j] is not None:
                        concat_len= len(arr[i]+arr[j])
                        if  concat_len > max_curr and set(arr[i]).intersection( set(arr[j])) == set():
                            max_curr=concat_len
                max_len= max(max_curr,max_len)
        return max_len

# @lc code=end
obj = Solution()
print( obj.maxLength(["abcdefghijklmnopqrstuvwxyz"]) )

