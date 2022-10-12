
from LList import MyLinkedList, Node


class Solution:
    def hasCycle(self, head: Node) -> bool:

        if head:
            slow = fast = head
            while(slow and fast and fast.next):
                slow = slow.next
                fast = fast.next.next
                if(slow == fast):
                    return True
        return False


s = Solution()
mylist = MyLinkedList(*[1,2,3,4,1,1,1,1])
# mylist.get_tail().Next = mylist.get_node(3)

print(s.hasCycle(mylist.get_node(0)))
