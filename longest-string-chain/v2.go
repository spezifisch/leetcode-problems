package v2

func isPredecessor(a, b string) bool {
	// a is the shorter string
	// abc, abac -> true
	// cba, bcad -> false

	// check isn't needed because the caller ensures this
	//if 1+len(a) != len(b) {
	//return false
	//}

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
	// table index = word length (16 max. + 1 so we can directly use word length as index)
	//       value = map of word => max. chain length for this word
	table := make([]map[string]int, 1+16)

	// sort words by length
	minWordLen := 17
	maxWordLen := 0
	for _, word := range words {
		// initialize map if needed
		if table[len(word)] == nil {
			table[len(word)] = map[string]int{}
		}

		// initialize with 0 and add 1 in the last line of this function,
		// that way we don't need to look at the words with the shortest length.
		table[len(word)][word] = 0

		if len(word) > maxWordLen {
			maxWordLen = len(word)
		}
		if len(word) < minWordLen {
			minWordLen = len(word)
		}
	}

	maxChain := 0
	var chainLen, newChainLen int
	// start iteration at the second-shortest word length
	for wordLen := 1 + minWordLen; wordLen < 1+maxWordLen; wordLen++ {
		for word := range table[wordLen] {
			// check all words with 1 characters less than the current word,
			// other ones can't be predecessors
			for prevWord, prevChainLen := range table[wordLen-1] {
				if isPredecessor(prevWord, word) {
					// we found a chain element
					chainLen = table[wordLen][word]
					newChainLen = prevChainLen + 1
					if newChainLen > chainLen {
						table[wordLen][word] = newChainLen

						if newChainLen > maxChain {
							maxChain = newChainLen
						}
					}
				}
			}
		}
	}

	return 1 + maxChain
}

// Runtime: 27 ms, faster than 81.76% of Go online submissions for Longest String Chain.
// Memory Usage: 6.9 MB, less than 42.94% of Go online submissions for Longest String Chain.
