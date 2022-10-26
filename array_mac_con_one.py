from collections import Counter
class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        max_count= 0
        _current_count= 0 
        for i in nums:
            if i == 1:
                _current_count += 1
                if(_current_count > max_count):
                    max_count= _current_count
            else:
                _current_count= 0
        
        return max_count
        


s1= Solution()
A = [1,1,0,0,1, 1,1,0,1]
print(s1.findMaxConsecutiveOnes(A))
