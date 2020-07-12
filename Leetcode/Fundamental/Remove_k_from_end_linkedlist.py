# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        helper_pointer = main_pointer = head
        prev = None

        while helper_pointer:
            if n < 1:
                prev = main_pointer
                main_pointer = main_pointer.next
                helper_pointer = helper_pointer.next
            else:
                n = n - 1
                helper_pointer = helper_pointer.next

        if prev is None and n < 1:
            head = head.next
            return head

        elif main_pointer and n < 1:
            prev.next = main_pointer.next
            main_pointer.next = None
            return head
        else:
            return head