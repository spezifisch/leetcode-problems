from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        if not len(deck):
            return []
        
        deck.sort()
        output = deque()
        output.append(deck.pop())
        while len(deck):
            output.rotate(1)
            output.appendleft(deck.pop())
            
        return list(output)
    
# Runtime: 48 ms, faster than 74.00% of Python3 online submissions for Reveal Cards In Increasing Order.
# Memory Usage: 13.4 MB, less than 5.80% of Python3 online submissions for Reveal Cards In Increasing Order.

