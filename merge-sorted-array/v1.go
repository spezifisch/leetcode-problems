package v1

func merge(nums1 []int, m int, nums2 []int, n int) {
	taken1 := 0
	taken2 := 0
	for i := 0; i < n+m; i++ {
		idx1 := m - 1 - taken1
		idx2 := n - 1 - taken2
		if idx1 < 0 || (idx1 >= 0 && idx2 >= 0 && nums1[idx1] < nums2[idx2]) {
			taken2++
			nums1[n+m-1-i] = nums2[idx2]
		} else {
			taken1++
			nums1[n+m-1-i] = nums1[idx1]
		}
	}
}

// Runtime: 5 ms, faster than 21.29% of Go online submissions for Merge Sorted Array.
// Memory Usage: 2.3 MB, less than 21.74% of Go online submissions for Merge Sorted Array.
