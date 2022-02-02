# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseList(self, head: ListNode, prev: ListNode = None) -> ListNode:
        if not head:
            return prev

        nxt = head.next
        head.next = prev
        return self.reverseList(nxt, head)


# Runtime: 44 ms, faster than 66.06% of Python3 online submissions for Reverse Linked List.
# Memory Usage: 20 MB, less than 5.22% of Python3 online submissions for Reverse Linked List.
