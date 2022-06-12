package v2

func maximumUniqueSubarray(nums []int) int {
	prefixSum := make([]int, len(nums))
	acc := 0
	lastIndex := map[int]int{}
	sliceStart := 0
	maxScore := 0

	var index, score int
	var ok bool
	for i, num := range nums {
		prefixSum[i] = acc
		acc += num

		index, ok = lastIndex[num]
		if ok {
			if index+1 > sliceStart {
				score = prefixSum[i] - prefixSum[sliceStart]
				if score > maxScore {
					maxScore = score
				}

				sliceStart = index + 1
			}
		}
		lastIndex[num] = i
	}

	score = acc - prefixSum[sliceStart]
	if score > maxScore {
		maxScore = score
	}
	return maxScore
}

// Runtime: 211 ms, faster than 80.77% of Go online submissions for Maximum Erasure Value.
// Memory Usage: 9.8 MB, less than 26.92% of Go online submissions for Maximum Erasure Value.
