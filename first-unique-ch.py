from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        _counter= Counter(s)
        char=''
        for k in _counter:
            if(_counter[k] == 1):
                char= k
                break
        if char:
            return s.find(char)
        else:
            return -1
                
        
        
s1= Solution()
print(s1.firstUniqChar("aabbcddee"))