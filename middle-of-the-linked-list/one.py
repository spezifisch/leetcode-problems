# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        count = 0
        node = head
        while node:
            count += 1
            node = node.next

        mid = count // 2

        count = 0
        node = head
        while node:
            if count == mid:
                return node

            count += 1
            node = node.next


# Runtime: 36 ms, faster than 57.52% of Python3 online submissions for Middle of the Linked List.
# Memory Usage: 13.2 MB, less than 5.04% of Python3 online submissions for Middle of the Linked List.
