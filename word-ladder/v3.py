from collections import deque
from functools import cache


def distance(a: str, b: str) -> int:
    diffs = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            diffs += 1
            if diffs >= 2:
                # we only need to know if the words have 0, 1 or more than 2 differences
                return 2
    return diffs


# cached version for distances to beginWord (ensure that b=beginWord)
@cache
def distance_to_begin(a: str, b: str) -> int:
    return distance(a, b)


class QueueItem:
    pathLen: int
    nodeWord: str


class Solution:
    def ladderLength(
        self, beginWord: str, endWord: str, wordList: list[str] | set[str]
    ) -> int:
        wordList = set(wordList)
        wordList.discard(beginWord)
        if endWord not in wordList:
            return 0

        fit = QueueItem()
        fit.pathLen = 0
        fit.nodeWord = endWord
        wordList.remove(endWord)

        q = deque([fit])
        while len(q):
            it = q.popleft()
            pathLen = it.pathLen + 1

            # special case when beginWord and endWord differ only by one character
            if pathLen == 1 and distance_to_begin(it.nodeWord, beginWord) == 1:
                return 2

            # get child nodes which have distance 1 to the current word
            childWords = []
            for word in wordList:
                d = distance(word, it.nodeWord)
                if d == 1:
                    # found a child word
                    childWords.append(word)

                    if distance_to_begin(word, beginWord) == 1:
                        # found a path!
                        return pathLen + 2

                    cit = QueueItem()
                    cit.pathLen = pathLen
                    cit.nodeWord = word
                    q.append(cit)

            for word in childWords:
                wordList.remove(word)

        return 0


# Runtime: 8445 ms, faster than 5.00% of Python3 online submissions for Word Ladder.
# Memory Usage: 15.7 MB, less than 60.38% of Python3 online submissions for Word Ladder.
