# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        count = 0
        mid_node = head
        node = head
        while node:
            node = node.next
            count += 1
            if count % 2 == 0:
                mid_node = mid_node.next
            
        return mid_node
            
# Runtime: 36 ms, faster than 57.52% of Python3 online submissions for Middle of the Linked List.
# Memory Usage: 12.8 MB, less than 5.04% of Python3 online submissions for Middle of the Linked List.

