# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        length = 0
        cur = head
        while cur:
            cur = cur.next
            length += 1

        if length <= 1:
            return []

        node_to_remove = length - n
        first = node_to_remove - 1
        second = node_to_remove + 1
        first_node = second_node = None

        if node_to_remove == 0:
            return head.next

        i = 0
        cur = head
        while cur:
            if i == first:
                first_node = cur
            elif i == second:
                second_node = cur
                break

            cur = cur.next
            i += 1

        first_node.next = second_node

        return head


# Runtime: 44 ms, faster than 49.47% of Python3 online submissions for Remove Nth Node From End of List.
# Memory Usage: 13.1 MB, less than 5.60% of Python3 online submissions for Remove Nth Node From End of List.
