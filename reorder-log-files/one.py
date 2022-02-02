from operator import itemgetter


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []
        for log in logs:
            words = log.split(" ", 2)
            try:
                int(words[1])
            except ValueError:
                words = log.split(" ", 1)
                letter_logs.append(words)
            else:
                digit_logs.append(log)

        letter_logs = sorted(letter_logs, key=itemgetter(1, 0))
        return [" ".join(log) for log in letter_logs] + digit_logs


# Runtime: 48 ms, faster than 42.40% of Python3 online submissions for Reorder Log Files.
# Memory Usage: 13.4 MB, less than 6.17% of Python3 online submissions for Reorder Log Files.
