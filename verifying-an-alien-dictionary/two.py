class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        self.order = order
        last_alien_word = None
        for word in words:
            alien_word = self.alien(word)
            if last_alien_word is not None and last_alien_word > alien_word:
                return False

            last_alien_word = alien_word

        return True

    def alien(self, word: str) -> str:
        alien_word = "".join([chr(ord("a") + self.order.find(c)) for c in word])
        return alien_word


# Runtime: 52 ms, faster than 32.89% of Python3 online submissions for Verifying an Alien Dictionary.
# Memory Usage: 13.3 MB, less than 5.45% of Python3 online submissions for Verifying an Alien Dictionary.
