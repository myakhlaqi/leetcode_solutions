#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
#     recursive solution
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        next = self.swapPairs(head.next.next)
        head.next.next = head
        first = head.next
        head.next = next
        return first
        
#     iterative solution
    def swapPairs1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        curr, prev = head , None
        while curr and curr.next:
            tmp = curr.next.next
            if curr == head:
                head = curr.next
            if prev:
                prev.next = curr.next
            curr.next.next = curr
            curr.next = tmp
            prev = curr
            curr = curr.next

        return head
                    
# @lc code=end

