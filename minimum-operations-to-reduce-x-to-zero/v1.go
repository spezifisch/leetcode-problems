package v1

func minOperations(nums []int, x int) int {
	// 0 = no solution found yet
	minSteps := 0

	// build prefix sum starting on the right-most element
	prefixSumRight := map[int]int{}
	sumRight := 0
	for i := 0; i < len(nums); i++ {
		// for i=0 this is the last element of nums, for i=1 second to last etc.
		sumRight += nums[len(nums)-1-i]
		if sumRight > x {
			// already too high and can only grow further
			break
		} else if sumRight == x {
			minSteps = i + 1 // found first candidate solution
			break
		}

		prefixSumRight[sumRight] = i + 1 // number of steps
	}

	// build prefix sum from left
	sumLeft := 0
	var wantedPrefixSumRight, stepsRight int
	var found bool
	for i, num := range nums {
		sumLeft += num
		if sumLeft > x {
			// too high, we can't build anything with this
			break
		} else if sumLeft == x {
			// found a candidate
			steps := i + 1
			if minSteps == 0 || steps < minSteps {
				minSteps = steps
			}
			break // it's already at the target value and can only go higher
		}

		// x = prefix sum left + prefix sum right
		// look if we have a matching partner on the right side for the current sumLeft
		wantedPrefixSumRight = x - sumLeft
		stepsRight, found = prefixSumRight[wantedPrefixSumRight]
		if found {
			steps := i + 1 + stepsRight
			// ensure that we don't count an array element twice
			if steps <= len(nums) {
				if minSteps == 0 || steps < minSteps {
					minSteps = steps
				}
			} else {
				break
			}
		}
	}

	if minSteps > 0 {
		return minSteps
	}
	return -1
}

// Runtime: 251 ms, faster than 30.77% of Go online submissions for Minimum Operations to Reduce X to Zero.
// Memory Usage: 14.8 MB, less than 7.69% of Go online submissions for Minimum Operations to Reduce X to Zero.
