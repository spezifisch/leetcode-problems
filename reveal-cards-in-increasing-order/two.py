class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        if not len(deck):
            return []

        deck.sort()
        output = [deck.pop()]
        while len(deck):
            output = output[-1:] + output[:-1]
            elem = deck.pop()
            output.insert(0, elem)

        return output


# Runtime: 80 ms, faster than 20.51% of Python3 online submissions for Reveal Cards In Increasing Order.
# Memory Usage: 13.4 MB, less than 5.80% of Python3 online submissions for Reveal Cards In Increasing Order.
