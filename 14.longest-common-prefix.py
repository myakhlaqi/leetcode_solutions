#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        min_len = min(len(s) for s in strs)
        for i in range(min_len):
            ch = strs[0][i]
            is_prefix = True
            for s in strs:
                if s[i] != ch:
                    is_prefix = False
                    break
            print(i,is_prefix,ch)
            if is_prefix:
                ans += ch
            else:
                break
        return ans
                    
        
# @lc code=end

