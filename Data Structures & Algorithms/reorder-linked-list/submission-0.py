# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #get the mid of list and split into 2 lists 
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None
        first = head

        #reverse the second list 
        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        reversed_second = prev

        # merge the first and reversed second
        while reversed_second:
            nxt1 = first.next
            nxt2 = reversed_second.next
            first.next = reversed_second
            reversed_second.next = nxt1
            first = nxt1
            reversed_second = nxt2


'''
1-2-3-4-5-6
break into two lists 
1-2-3   4-5-6
reverse the second list 
1-2-3   6-5-4
alt merge the lists 
1-6-2-5-3-4  
'''
        