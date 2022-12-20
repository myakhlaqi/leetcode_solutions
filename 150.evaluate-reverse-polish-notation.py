#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
import operator

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.floordiv,  # use operator.div for Python 2
}
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            # print(stack)
            if t in {"+","-","*","/"}:
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(int(ops[t](num1, num2)))
            else:
                stack.append(int(t))
        return stack.pop()
            
            
        
        
# @lc code=end

