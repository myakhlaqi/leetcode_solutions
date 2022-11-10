import sys


class Solution:
    def get_min(self,nums,start,end):
        min_val=(sys.maxsize,-1)
        for i in range(start,end):
            if nums[i]<min_val[0]:
                min_val=(nums[i],i)
        return min_val
    def totalCost(self, costs, k: int, candidates: int):
        right_start = max(len(costs)- candidates, candidates)
        lowest_cost=0
        for _ in range(k):
            left_min= self.get_min(costs,0,min(candidates,len(costs)))
            right_min= self.get_min(costs,right_start,len(costs))
            print(left_min,right_min)
            if left_min[0] < right_min[0] or left_min[0] <= right_min[0]:
                lowest_cost+=left_min[0]
                del costs[left_min[1]]
            else:
                lowest_cost+=right_min[0]
                del costs[right_min[1]]
            right_start = max(len(costs)- candidates, candidates)
        return lowest_cost
obj=Solution()
print(obj.totalCost([1,2,4,1],3,3))