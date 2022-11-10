#
# @lc app=leetcode id=498 lang=python3
#
# [498] Diagonal Traverse
#

# @lc code=start
class Solution:
    def findDiagonalOrder(self, mat) :
        n=len(mat)
        m=len(mat[0])
        ans=[]
        row,col=0,0
        for d in range(m+n-1):
            temp=[]
            if d < n:
                row=d 
                col=0
            else:
                row= n-1
                col= d-row
            while row>=0 and col<m:
                temp.append(mat[row][col])
                row-=1
                col+=1
            if d % 2==0:
                ans.extend(temp)
            else:
                ans.extend(temp[::-1])
        
        return ans
                    
                    
# @lc code=end
obj = Solution()
# mat= [[1,2,6,7],[3,5,8,13],[4,9,12,14],[10,11,15,16]]
mat = [[6,9,7]]
print(obj.findDiagonalOrder(mat))

