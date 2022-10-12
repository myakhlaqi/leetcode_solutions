#
# @lc app=leetcode id=653 lang=python3

# [653] Two Sum IV - Input is a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    seen= set()
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if root is None:
            return False
        second_num=k- root.val
        # print(root.val, self.seen)
        
        if root.val in self.seen:
            return True
                
        self.seen.add(second_num)
        is_in_left= self.findTarget(root.left,k)
        if is_in_left:
            return True
        is_in_right=self.findTarget(root.right,k)        
        if is_in_right:
            return True
        return False
            
        
# obj= Solution()
# print(obj.findTarget([5,3,6,2,4,None,7]),9)
# @lc code=end

