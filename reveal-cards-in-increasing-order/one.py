from collections import deque


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        reference_output = []

        working_deck = deque(range(len(deck)))
        while len(working_deck):
            reference_output.append(working_deck.popleft())
            working_deck.rotate(-1)

        output = [None] * len(deck)
        for i, elem in enumerate(sorted(deck)):
            output_idx = reference_output[i]
            output[output_idx] = elem

        return output


# Runtime: 48 ms, faster than 74.00% of Python3 online submissions for Reveal Cards In Increasing Order.
# Memory Usage: 13.1 MB, less than 5.80% of Python3 online submissions for Reveal Cards In Increasing Order.
