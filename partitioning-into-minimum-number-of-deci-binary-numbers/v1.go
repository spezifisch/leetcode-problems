package v1

func minPartitions(n string) int {
	highestDigit := 0
	var digit int
	for _, r := range n {
		digit = int(r) - int('0')
		if digit > highestDigit {
			highestDigit = digit
		}
	}

	return highestDigit
}

// Runtime: 13 ms, faster than 75.44% of Go online submissions for Partitioning Into Minimum Number Of Deci-Binary Numbers.
// Memory Usage: 6.7 MB, less than 47.37% of Go online submissions for Partitioning Into Minimum Number Of Deci-Binary Numbers.
