class Solution:
    MORSE = [
        ".-",
        "-...",
        "-.-.",
        "-..",
        ".",
        "..-.",
        "--.",
        "....",
        "..",
        ".---",
        "-.-",
        ".-..",
        "--",
        "-.",
        "---",
        ".--.",
        "--.-",
        ".-.",
        "...",
        "-",
        "..-",
        "...-",
        ".--",
        "-..-",
        "-.--",
        "--..",
    ]

    @staticmethod
    def toMorse(word: str) -> str:
        word = [Solution.MORSE[ord(c) - ord("a")] for c in word]
        return "".join(word)

    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        unique = list()

        for word in words:
            unique.append(Solution.toMorse(word))

        return len(set(unique))


# Runtime: 40 ms, faster than 57.19% of Python3 online submissions for Unique Morse Code Words.
# Memory Usage: 13.2 MB, less than 5.36% of Python3 online submissions for Unique Morse Code Words.
