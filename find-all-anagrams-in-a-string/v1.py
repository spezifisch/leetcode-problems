class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        p = sorted(p)
        cache = {}
        result = []

        for i_start in range(len(s) - len(p) + 1):
            chunk = s[i_start : i_start + len(p)]
            hit = cache.get(chunk)
            if hit is None:
                sorted_chunk = sorted(chunk)

                match = sorted_chunk == p
                cache[chunk] = match
                if match:
                    result.append(i_start)
            else:
                if hit is True:
                    result.append(i_start)

        return result


# Runtime: 1924 ms, faster than 8.04% of Python3 online submissions for Find All Anagrams in a String.
# Memory Usage: 122.9 MB, less than 10.05% of Python3 online submissions for Find All Anagrams in a String.
