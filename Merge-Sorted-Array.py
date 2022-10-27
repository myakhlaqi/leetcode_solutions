# https://leetcode.com/explore/learn/card/fun-with-arrays/525/inserting-items-into-an-array/3253/
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
#-----------------------------in-place code-----------------------------------------

        j= n-1
        i= m-1
        ix= (m + n) -1
        while i>=0 and j>=0:
            if(nums2[j] > nums1[i]):
                nums1[ix]=nums2[j]
                j-=1
                ix-=1
            else:
                nums1[ix]=nums1[i]
                i-=1
                ix-=1
            #print(nums1)
        if(i<0):
            while j>=0:
                nums1[ix]=nums2[j]
                j-=1
                ix-=1
        else:
            while i>=0:
                nums1[ix]=nums1[i]
                i-=1
                ix-=1
            
#--------------------------extra memory usage---------------------        
#         ans=[]
#         i=0 # index for num1
#         j=0 # index for num2

#         while i<m and j<n:
#             if(nums1[i]<=nums2[j]):
#                 ans.append(nums1[i])
#                 i+=1
#             else:
#                 ans.append(nums2[j])
#                 j+=1
#             #print(ans)
#         if j<n:
#             for x in range(j,n):
#                 ans.append(nums2[x])
#         else:
#             for x in range(i,m):
#                 ans.append(nums1[x])
#         for i in range(n+m):
#             nums1[i]=ans[i]
        
            
            
            
