# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return []

        return self.swap_two(None, head, head.next)

    def swap_two(self, previous: ListNode, one: ListNode, two: ListNode):
        if not two:
            return one

        next_pair = two.next

        if previous:
            previous.next = two

        two.next = one
        one.next = next_pair

        if next_pair:
            self.swap_two(one, next_pair, next_pair.next)

        return two


# Runtime: 40 ms, faster than 37.95% of Python3 online submissions for Swap Nodes in Pairs.
# Memory Usage: 13.4 MB, less than 5.04% of Python3 online submissions for Swap Nodes in Pairs.
