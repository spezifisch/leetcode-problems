package v2

func minPartitions(n string) int {
	i0 := int('0')
	var digit, highestDigit int
	for _, r := range n {
		digit = int(r) - i0
		if digit > highestDigit {
			highestDigit = digit
		}
	}

	return highestDigit
}

// Runtime: 10 ms, faster than 87.72% of Go online submissions for Partitioning Into Minimum Number Of Deci-Binary Numbers.
// Memory Usage: 6.4 MB, less than 94.74% of Go online submissions for Partitioning Into Minimum Number Of Deci-Binary Numbers.
