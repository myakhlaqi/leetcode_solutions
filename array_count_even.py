import math

class Solution:
    def count_digit(self, n):
        return len(str(n))

    def count_digit_log10(self, n):
        digits = 0
        if n > 0:
            digits = int(math.log10(n))+1
        elif n == 0:
            digits = 1
        else:
            digits = int(math.log10(-n))+2  # +1 if you don't count the '-'
        return digits;

    def findNumbers(self, nums):
        count_even = sum([1 for i in nums  if(self.count_digit_log10(i) % 2 == 0)])
        # for i in nums:
        #     if(self.count_digit_log10(i) % 2 == 0):
        #         count_even += 1

        return count_even
