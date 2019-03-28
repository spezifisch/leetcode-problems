class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        needed_letters = [c.lower() for c in licensePlate if c.isalpha()]
        words = sorted(words, key=lambda word: len(word))
        
        for word in words:
            present_letters = list(word)
            try:
                for letter in needed_letters:
                    present_letters.remove(letter)
            except ValueError:
                continue
            else:
                return word
            
        assert(False)
        
# Runtime: 60 ms, faster than 73.36% of Python3 online submissions for Shortest Completing Word.
# Memory Usage: 13.3 MB, less than 6.67% of Python3 online submissions for Shortest Completing Word.

