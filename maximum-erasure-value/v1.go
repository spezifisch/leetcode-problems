package v1

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
			score = prefixSum[i] - prefixSum[sliceStart]
			if score > maxScore {
				maxScore = score
			}

			if index+1 > sliceStart {
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

// Runtime: 277 ms, faster than 50.00% of Go online submissions for Maximum Erasure Value.
// Memory Usage: 10.1 MB, less than 23.08% of Go online submissions for Maximum Erasure Value.
