#
# @lc app=leetcode id=901 lang=python3
#
# [901] Online Stock Span
#

# @lc code=start
class StockSpanner:

    def __init__(self):
        self.span=[]

    def next(self, price: int) -> int:
        self.span.append(price)
        max_k=k=0
        for p in self.span[::-1]:
            if p <= price:
                k+=1
            else:
            
                # print(price, p, k, max_k)
                break
            max_k = max (max_k,k)
        # max_k = max (max_k, k)
        return max_k


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(100)
# @lc code=end

