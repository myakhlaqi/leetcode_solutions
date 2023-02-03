from LList import MyLinkedList,Node

def reverse(head):
    if not head.next:
        return head
    new_head=reverse(head.next)
    head.next.next=head
    head.next=None
    return new_head

def isPalindrome(head) -> bool:
    _,head = reverse(head)
    curr = head
    while curr:
        print(curr.val)
        curr=curr.next

my_list=MyLinkedList(*[1,2,3])
_,my_list.head = reverse(my_list.head)
print(my_list)
