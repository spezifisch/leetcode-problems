# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ret_base = None
        ret_current = None
        left = l1
        right = l2
        
        while left or right:
            new_node = None
            if left and (not right or right.val >= left.val):
                new_node = ListNode(left.val)
                left = left.next
            elif right or not left:
                new_node = ListNode(right.val)
                right = right.next
            else:
                break

            if ret_current:
                ret_current.next = new_node
                ret_current = ret_current.next
            else:
                ret_base = new_node
                ret_current = ret_base
            
        return ret_base
    
# Runtime: 48 ms, faster than 52.71% of Python3 online submissions for Merge Two Sorted Lists.
# Memory Usage: 13.2 MB, less than 5.06% of Python3 online submissions for Merge Two Sorted Lists.

