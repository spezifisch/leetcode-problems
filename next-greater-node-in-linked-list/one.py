# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from bisect import bisect_left
from collections import deque


class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        stack_idx = deque()
        stack_val = deque()
        ans = []
        list_idx = 0
        while head:
            idx = bisect_left(stack_val, head.val)
            for i in range(idx):
                ans[stack_idx[i]] = head.val

            for i in range(idx):
                stack_idx.popleft()
                stack_val.popleft()

            stack_idx.appendleft(list_idx)
            stack_val.appendleft(head.val)
            list_idx += 1
            ans.append(0)
            head = head.next

        return ans


# Runtime: 540 ms, faster than 7.89% of Python3 online submissions for Next Greater Node In Linked List.
# Memory Usage: 17.8 MB, less than 100.00% of Python3 online submissions for Next Greater Node In Linked List.
