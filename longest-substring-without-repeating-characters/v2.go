package v2

func lengthOfLongestSubstring(s string) int {
	lastOccurrence := map[rune]int{}
	substringStartIdx := 0
	longestSubstring := 0

	var lastOccurrenceIdx, thisLen int
	var ok bool
	for i, c := range s {
		lastOccurrenceIdx, ok = lastOccurrence[c]
		if ok && lastOccurrenceIdx >= substringStartIdx {
			substringStartIdx = lastOccurrenceIdx + 1
		}
		lastOccurrence[c] = i

		thisLen = i - substringStartIdx + 1
		if thisLen > longestSubstring {
			longestSubstring = thisLen
		}
	}

	return longestSubstring
}

// Runtime: 10 ms, faster than 62.17% of Go online submissions for Longest Substring Without Repeating Characters.
// Memory Usage: 3.2 MB, less than 45.79% of Go online submissions for Longest Substring Without Repeating Characters.
