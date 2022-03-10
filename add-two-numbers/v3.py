# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # challenge: i'm trying to reuse the input nodes
        carry = 0
        first_l1 = output_node = l1
        first_l2 = l2
        while l1 or l2 or carry:
            a = b = 0
            if l1:
                a = l1.val
            if l2:
                b = l2.val

            # add with carry
            s = a + b + carry
            if s > 9:
                carry = 1
                s -= 10
            else:
                carry = 0

            # next nodes
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

            # put into output
            output_node.val = s
            if not l1 and not l2 and not carry:
                # end of inputs. if carry is 0 we don't need another loop iteration
                output_node.next = None
            elif output_node.next:
                # take another one from l1's chain
                output_node = output_node.next
            else:
                # switch to l2's chain
                output_node.next = first_l2
                output_node = first_l2

        return first_l1


# Runtime: 83 ms, faster than 67.14% of Python3 online submissions for Add Two Numbers.
# Memory Usage: 13.9 MB, less than 93.12% of Python3 online submissions for Add Two Numbers.
