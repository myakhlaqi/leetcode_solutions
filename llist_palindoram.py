from LList import MyLinkedList, Node


def reverse(head):
    if not head.next:
        return head
    new_head = reverse(head.next)
    head.next.next = head
    head.next = None
    return new_head

# O(n) time and O(n) memory
def isPalindrome(head) -> bool:
    curr = head

    def check(curr_head):
        nonlocal curr
        if curr_head is not None:
            if not check(curr_head.next):
                return False
            if curr_head.val != curr.val:
                return False
            curr=curr.next
        return True
    return check(head)

def isPalindrome2(head) -> bool:
    if head is None or head.next is None:
        return True
    # find the tail (fast) and the mid element (slow)
    slow = head
    fast= head.next
    tail= None
    size=0
    while fast is not None and fast.next is not None:
        tail = fast
        slow = slow.next
        fast = fast.next.next
        size+=1
    if fast is None:
        tail = tail.next
    else:
        tail= fast
    # reverse the second half of the list after slow to the tail
    curr = slow.next
    while curr!=tail:
        slow.next = curr.next
        curr.next = tail.next
        tail.next = curr
        
        curr=slow.next
    # compare the elements in both sides
    start = head
    while curr is not None:
        if curr.val != start.val:
            return False
        curr=curr.next
        start=start.next
    return True
    
        


# my_list = MyLinkedList(*[1,2,3,1])

# print(my_list)

# print(my_list.head.val)
print(isPalindrome2(my_list.head))
