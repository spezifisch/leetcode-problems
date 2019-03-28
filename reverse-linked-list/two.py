# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        while head:
            nxt = head.next
            head.next = prev
            
            prev = head
            head = nxt
            
        return prev
    
# Runtime: 44 ms, faster than 66.06% of Python3 online submissions for Reverse Linked List.
# Memory Usage: 14.3 MB, less than 33.33% of Python3 online submissions for Reverse Linked List.

