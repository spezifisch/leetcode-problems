package v1

func isPredecessor(a, b string) bool {
	// a is the shorter string
	// abc, abac -> true
	// cba, bcad -> false
	if 1+len(a) != len(b) {
		return false
	}
	missing := 0
	posA := 0
	for posB := range b {
		if posA == len(a) {
			break
		} else if b[posB] != a[posA] {
			if missing > 0 {
				return false
			}
			missing++
		} else {
			posA++
		}
	}
	return true
}

func longestStrChain(words []string) int {
	if !isPredecessor("abc", "abac") || isPredecessor("abac", "abc") || isPredecessor("cba", "bcad") {
		panic("assert")
	}

	maxChain := 0
	table := make([]map[string]int, 1+16) // 1-indexed
	for i := range table {
		table[i] = map[string]int{}
	}

	minWordLen := 17
	maxWordLen := 0
	for _, word := range words {
		table[len(word)][word] = 0

		if len(word) > maxWordLen {
			maxWordLen = len(word)
		}
		if len(word) < minWordLen {
			minWordLen = len(word)
		}
	}

	for wordLen := 1 + minWordLen; wordLen < 1+maxWordLen; wordLen++ {
		for word := range table[wordLen] {
			for prevWord, prevChainLen := range table[wordLen-1] {
				if isPredecessor(prevWord, word) {
					if prevChainLen+1 > table[wordLen][word] {
						table[wordLen][word] = prevChainLen + 1

						if table[wordLen][word] > maxChain {
							maxChain = table[wordLen][word]
						}
					}
				}
			}
		}
	}

	return 1 + maxChain
}

// Runtime: 50 ms, faster than 31.76% of Go online submissions for Longest String Chain.
// Memory Usage: 6.8 MB, less than 42.94% of Go online submissions for Longest String Chain.
