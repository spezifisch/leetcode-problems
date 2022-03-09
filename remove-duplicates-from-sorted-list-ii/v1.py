# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        last_good_node = None
        last_node = None
        node = head
        while node:
            same_as_next = node.next and node.val == node.next.val

            if last_node:
                same_as_last = node.val == last_node.val

                if not same_as_last and not same_as_next:
                    last_good_node = node
                elif same_as_last:
                    if not last_good_node:
                        # new head
                        head = node.next
                    elif not node.next:
                        # new tail without this node
                        last_good_node.next = None
                    else:
                        last_good_node.next = node.next
            else:
                # first round
                if not same_as_next:
                    last_good_node = node

            last_node = node
            node = node.next

        return head


# Runtime: 63 ms, faster than 41.57% of Python3 online submissions for Remove Duplicates from Sorted List II.
# Memory Usage: 13.9 MB, less than 54.61% of Python3 online submissions for Remove Duplicates from Sorted List II.
