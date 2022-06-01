package main

func runningSum(nums []int) []int {
	ret := make([]int, len(nums))
	for i, v := range nums {
		if i > 0 {
			ret[i] = ret[i-1] + v
		} else {
			ret[i] = v
		}
	}
	return ret
}

// Runtime: 0 ms, faster than 100.00% of Go online submissions for Running Sum of 1d Array.
// Memory Usage: 2.8 MB, less than 47.22% of Go online submissions for Running Sum of 1d Array.
