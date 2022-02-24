from sortedcontainers import SortedDict

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        # just because I like sortedcontainers
        lol = SortedDict()
        node = head
        while node:
            elem = lol.get(node.val, [])
            elem.append(node)
            lol[node.val] = elem

            node = node.next

        head = None
        prev_node = None
        for elem in lol.values():
            for node in elem:
                if head is None:
                    head = node

                if prev_node is not None:
                    prev_node.next = node

                prev_node = node

        prev_node.next = None

        return head


# Runtime: 477 ms, faster than 57.05% of Python3 online submissions for Sort List.
# Memory Usage: 39 MB, less than 9.88% of Python3 online submissions for Sort List.
