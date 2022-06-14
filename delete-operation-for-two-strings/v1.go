package v1

func minDistance(word1 string, word2 string) int {
	currentRow := make([]int, len(word2)+1)
	lastRow := make([]int, len(word2)+1)

	for _, r1 := range word1 {
		for j, r2 := range word2 {
			if r1 == r2 {
				currentRow[1+j] = 1 + lastRow[j]
			} else {
				if lastRow[1+j] > currentRow[j] {
					currentRow[1+j] = lastRow[1+j]
				} else {
					currentRow[1+j] = currentRow[j]
				}
			}
		}

		currentRow, lastRow = lastRow, currentRow
	}

	longestCommonSubsequence := lastRow[len(lastRow)-1]
	needed1 := len(word1) - longestCommonSubsequence
	needed2 := len(word2) - longestCommonSubsequence
	return needed1 + needed2
}

// Runtime: 4 ms, faster than 100.00% of Go online submissions for Delete Operation for Two Strings.
// Memory Usage: 3 MB, less than 100.00% of Go online submissions for Delete Operation for Two Strings.
