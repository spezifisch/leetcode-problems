package v2

func twoSum(numbers []int, target int) []int {
	a := 0
	b := len(numbers) - 1

	var sum int
	for a < b {
		sum = numbers[a] + numbers[b]
		if sum > target {
			b--
		} else if sum < target {
			a++
		} else {
			// found it
			return []int{a + 1, b + 1}
		}
	}

	return []int{}
}

// Runtime: 26 ms, faster than 19.73% of Go online submissions for Two Sum II - Input Array Is Sorted.
// Memory Usage: 5.5 MB, less than 50.03% of Go online submissions for Two Sum II - Input Array Is Sorted.
