#
# @lc app=leetcode id=249 lang=python3
#
# [249] Group Shifted Strings
#

# @lc code=start
from collections import defaultdict
from turtle import distance
class Solution:
    
    def hash(self,word):
        # return str(len(word))+"-"+str(sum([ ord(ch)-ord('a') for ch in word ]))
        key=tuple()
        for i in range(len(word)-1):
            distance= ord(word[i+1]) - ord(word[i]) 
            key += (26+distance,) if distance<0 else (distance,)
        return key
        
    def groupAnagrams(self, strs):
        word_dic=defaultdict(list)
        for s in strs:
            key=self.hash(s)
            word_dic[key].append(s)

        return word_dic.values()
             
# @lc code=end
obj=Solution()
strs=["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
print(obj.groupAnagrams(strs))