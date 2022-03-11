# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or not head:
            return head

        # connect tail to head
        node = head
        node_count = 1
        while node.next:
            node_count += 1
            node = node.next

        node.next = head

        cut_at = node_count - (k % node_count)
        if cut_at == 0:
            return head

        # break the cycle at given k
        prev_node = None
        node = head
        for i in range(cut_at):
            prev_node = node
            node = node.next

        new_head = node
        prev_node.next = None
        return new_head


# Runtime: 49 ms, faster than 63.02% of Python3 online submissions for Rotate List.
# Memory Usage: 14 MB, less than 32.21% of Python3 online submissions for Rotate List.
