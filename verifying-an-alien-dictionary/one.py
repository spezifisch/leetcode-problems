class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        self.order = order
        alien_words = [self.alien(word) for word in words]
        
        return alien_words == sorted(alien_words)
    
    def alien(self, word: str) -> str:
        alien_word = "".join([chr(ord("a") + self.order.find(c)) for c in word])
        return alien_word
    
# Runtime: 56 ms, faster than 27.20% of Python3 online submissions for Verifying an Alien Dictionary.
# Memory Usage: 13.2 MB, less than 5.45% of Python3 online submissions for Verifying an Alien Dictionary.

