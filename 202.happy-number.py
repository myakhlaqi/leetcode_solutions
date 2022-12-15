#
# @lc app=leetcode id=202 lang=python3
## [202] Happy Number
#
# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        while n!=1 and n not in seen:
            seen.add(n)
            n = sum(int(x)**2 for x in str(n) if x!='0') #log(n)
        return n==1
    def test_Happy():
        ans=set()
        for i in range(1000):
            seen=set()
            n=i
            while n!=1 and n not in seen:
                seen.add(n)
                n = sum(int(x)**2 for x in str(n) if x!='0') #log(n)
            print(f"{i}-{seen}")
            ans.add(n)
        #print(f"Answer:{ans}")

# @lc code=end

