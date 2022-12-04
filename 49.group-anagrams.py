#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
from collections import defaultdict
class Solution:
    
#     def hash(self,word):
#         # return str(len(word))+"-"+str(sum([ ord(ch)-ord('a') for ch in word ]))
#         key=[0]*26
#         for ch in word:
#             key[ord(ch)-ord('a')]+=1
#         return tuple([len(word)]+key)
        
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dic=defaultdict(list)
        for word in strs:
            key=[0]*26
            for ch in word:
                key[ord(ch)-ord('a')]+=1
            word_dic[tuple(key)].append(word)
        # print((word_dic))
        return word_dic.values()
             
# @lc code=end

