# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head
        
        new_head = None
        node = head
        while node:
            # set head to first node without val
            if new_head is None:
                if node.val != val:
                    new_head = node
            
            # get new next node
            next_node = node.next
            while next_node:
                if next_node.val != val:
                    break
                    
                # node needs to be removed
                next_node = next_node.next
            
            # replace next node
            if next_node != node.next:
                node.next = next_node
            
            node = next_node
        
        return new_head

# Runtime: 68 ms, faster than 78.34% of Python3 online submissions for Remove Linked List Elements.
# Memory Usage: 17.2 MB, less than 26.69% of Python3 online submissions for Remove Linked List Elements.

