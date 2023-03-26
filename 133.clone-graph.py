#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        stack = [node]
        first_copy_node = Node(node.val)
        # A dictionary that maps the original node to the copy node.
        visited = {node : first_copy_node}
        while stack:
            curr_node = stack[-1]
            
            copy = visited[curr_node]
            # for every visited node n in current node neighbors
            # add the copy nodes to the current copy node neighbors
            for n in curr_node.neighbors & visited.keys:
                if n not in copy.neighbors:
                    copy.neighbors.append( visited[n])

            unseen_neighbor = (set(curr_node.neighbors) - visited.keys)[0]
            if unseen_neighbor:
                stack.append(unseen_neighbor)
                # Creating a new node with the value of the unseen neighbor.
                visited[unseen_neighbor] = Node(unseen_neighbor.val)
            else:
                stack.pop()
        return first_copy_node
                    
# @lc code=end

