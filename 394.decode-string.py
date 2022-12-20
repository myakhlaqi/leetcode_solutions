#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i, ch in enumerate(s):
            print(ch,stack)
            if ch == '[':
                continue
            elif ch == ']' :
                str1 = stack.pop()
                number = int(stack.pop())
                stack.append( str1 * number )
                tmp_str = ""
                while stack and stack[-1].isalpha():
                    tmp_str = stack.pop() + tmp_str
                stack.append(tmp_str)
                    
            elif ch.isdigit() and len(stack) > 0 and s[i-1] != '[' and stack[-1].isdigit():
                    stack[-1] += ch
            elif ch.isalpha() and len(stack) > 0 and stack[-1].isalpha():
                stack[-1] += ch
            else: 
                stack.append(ch)

        if len(stack) > 1:
            str1 = stack.pop()
            number = int(stack.pop())
            stack[-1] += str1 * number
        return stack[0]

                    
# @lc code=end

