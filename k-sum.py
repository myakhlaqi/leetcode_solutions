class Solution:
    def kSum(self, nums: list[int], k: int) -> int:
        ans = [0]
        ans.append(nums)
        n = len(nums)
        for i in range(2,n):
            
            csum= sum([nums[x] for x in range(0,n,i)])
            ans.append(csum)
            ans.sort(reverse = True)
            print(ans)
        return ans

s= Solution()
A=[2,4,-2]
print(s.kSum(A,5))
        
        
