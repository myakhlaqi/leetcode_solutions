#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#

# @lc code=start
class Solution:
    def say(self,s):
        counter=0
        prev=s[0]
        ans=""
        for ch in s:
            if ch != prev:
                ans+=str(counter)+prev
                counter=1
                prev=ch
            else:
                counter+=1
        ans+=str(counter)+prev
        return ans
    def countAndSay(self, n: int) -> str:
        return "1" if n == 1 else self.say(self.countAndSay(n-1))
        
# @lc code=end
obj=Solution()
print(obj.countAndSay(5))
