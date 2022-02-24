# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insert(self, node: ListNode) -> None:
        if node.val < self.head.val:
            # new head
            node.next = self.head
            self.head = node
            return

        insert_after = self.head
        while insert_after:
            if insert_after.next is None:
                # we found the end
                break

            if insert_after.next == node:
                # we found ourself
                break

            if insert_after.next.val > node.val:
                # next node is bigger than ours
                break

            insert_after = insert_after.next

        node.next = insert_after.next
        insert_after.next = node

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        self.head = head
        node = head
        while node:
            next_node = node.next
            node.next = None

            if node != self.head:
                self.insert(node)

            node = next_node

        return self.head


# Time Limit Exceeded
