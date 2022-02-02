# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        after = head
        for i in range(n):
            after = after.next

        if after is None:
            return head.next

        before = head

        while after.next:
            after = after.next
            before = before.next

        before.next = before.next.next

        return head


# Runtime: 44 ms, faster than 49.47% of Python3 online submissions for Remove Nth Node From End of List.
# Memory Usage: 13.3 MB, less than 5.60% of Python3 online submissions for Remove Nth Node From End of List.
