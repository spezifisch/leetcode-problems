class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurence = {}

        for i, c in enumerate(s):
            last_occurence[c] = i

        parts = []
        start = end = None
        for i, c in enumerate(s):
            if start is None:
                # start a new part. it has to go at least until the last occ. of the same char
                start = i
                end = last_occurence[c]

            end = max(end, last_occurence[c])

            if i == end:
                # a part is complete
                parts.append(end - start + 1)
                start = None

        return parts


# Runtime: 47 ms, faster than 74.64% of Python3 online submissions for Partition Labels.
# Memory Usage: 13.9 MB, less than 78.97% of Python3 online submissions for Partition Labels.
