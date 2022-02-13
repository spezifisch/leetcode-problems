from collections import deque


def distance(a: str, b: str) -> int:
    assert len(a) == len(b)
    diffs = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            diffs += 1
            if diffs >= 2:
                # we only need to know if the words have 0, 1 or more than 2 differences
                return 2
    return diffs


class State:
    path: list[str]
    pathLen: int
    childrenWords: list[str]


class QueueItem:
    path: list[str]
    pathLen: int
    nodeWord: str


def solve(it: QueueItem, wordList: list[str], usedWords: set[str]) -> State:
    s = State()
    s.path = []
    # s.path = it.path + [it.nodeWord]
    s.pathLen = it.pathLen + 1
    # s.subWordList = []
    s.childrenWords = []
    for word in wordList:
        if word in usedWords:
            continue

        d = distance(word, it.nodeWord)
        if d == 1:
            s.childrenWords.append(word)
        # elif d > 1:
        #    s.subWordList.append(word)

    return s


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList:
            return 0
        if beginWord in wordList:
            wordList.remove(beginWord)

        begin_distances = {}

        fit = QueueItem()
        fit.path = []
        fit.pathLen = 0
        fit.nodeWord = endWord

        usedWords = {endWord}
        q = deque([fit])
        while len(q):
            it = q.popleft()

            if it.pathLen == 0 and distance(it.nodeWord, beginWord) == 1:
                # print("found direct", *it.path, it.nodeWord, beginWord)
                return 2

            s = solve(it, wordList, usedWords)

            for childWord in s.childrenWords:
                begin_distance = begin_distances.get(childWord)
                if begin_distance is None:
                    begin_distance = distance(childWord, beginWord)
                    begin_distances[childWord] = begin_distance

                if begin_distance == 1:
                    # found it!
                    # print("found", *s.path, childWord, beginWord)
                    return s.pathLen + 2

                usedWords.add(childWord)

                cit = QueueItem()
                cit.path = s.path
                cit.pathLen = s.pathLen
                cit.nodeWord = childWord
                q.append(cit)

        return 0


# Runtime: 9686 ms, faster than 5.00% of Python3 online submissions for Word Ladder.
# Memory Usage: 15.3 MB, less than 71.93% of Python3 online submissions for Word Ladder.
