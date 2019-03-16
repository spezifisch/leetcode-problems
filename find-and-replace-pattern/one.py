class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        return list(filter(lambda word: self.patterned(word, pattern), words))
        
    @staticmethod
    def patterned(word: str, pattern: str) -> bool:
        pattern_to_word = {}
        for i, c_pat in enumerate(pattern):
            if c_pat in pattern_to_word:
                if pattern_to_word[c_pat] != word[i]:
                    return False
            elif word[i] in pattern_to_word.values():
                return False
            else:
                pattern_to_word[c_pat] = word[i]
                
        return True

# Runtime: 40 ms, faster than 57.28% of Python3 online submissions for Find and Replace Pattern.
# Memory Usage: 13.1 MB, less than 5.00% of Python3 online submissions for Find and Replace Pattern.

