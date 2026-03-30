# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # split list 
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next

        second = slow.next
        slow.next = None

        # reverse the second list 
        prev = None
        cur = second
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        reversed_second = prev

        # alt merge the 2 lists 
        first = head
        while first and reversed_second:
            n1 = first.next
            n2 = reversed_second.next

            first.next = reversed_second
            reversed_second.next = n1

            first = n1
            reversed_second = n2
        
        
        