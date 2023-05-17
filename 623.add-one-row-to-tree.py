#
# @lc app=leetcode id=623 lang=python3
#
# [623] Add One Row to Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRowRec(self, root, depth):
        if root is None:
            return None
        if depth == self.depth-1:
            l = root.left
            r = root.right

            new_left = TreeNode(self.val)
            new_right = TreeNode(self.val)

            new_left.left = l
            new_right.right = r

            root.left = new_left
            root.right = new_right
            
        self.addOneRowRec(root.left, depth + 1)
        self.addOneRowRec(root.right,depth + 1)
        return root

    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        self.depth = depth
        self.val = val
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            root = new_root
        else:
            root = self.addOneRowRec(root,1)
        return root

# @lc code=end
