# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    @staticmethod
    def llToNumber(l):
        val = 0
        exp = 0
        while l:
            val += l.val * 10**exp
            exp += 1
            l = l.next
        return val    
    
    @staticmethod
    def numberToLL(val):
        # start with biggest exponent
        exp = len(str(val)) - 1
        ll = ListNode(int(val / 10**exp))
        exp -= 1
        while exp >= 0:
            old_ll = ll
            val -= ll.val * 10**(exp+1)
            new_ll = ListNode(int(val / 10**exp))
            new_ll.next = old_ll
            ll = new_ll
            exp -= 1
        return ll
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        x1 = self.llToNumber(l1)
        x2 = self.llToNumber(l2)
        return self.numberToLL(x1+x2)
        
# Runtime: 144 ms, faster than 37.96% of Python3 online submissions for Add Two Numbers.
# Memory Usage: 13.2 MB, less than 5.21% of Python3 online submissions for Add Two Numbers.

