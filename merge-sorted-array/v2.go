package v2

func merge(nums1 []int, m int, nums2 []int, n int) {
	idx1 := m - 1
	idx2 := n - 1
	nm := n + m
	for i := 0; i < nm; i++ {
		if idx1 < 0 || (idx1 >= 0 && idx2 >= 0 && nums1[idx1] < nums2[idx2]) {
			nums1[nm-1-i] = nums2[idx2]
			idx2--
		} else {
			nums1[nm-1-i] = nums1[idx1]
			idx1--
		}
	}
}

// Runtime: 0 ms, faster than 100.00% of Go online submissions for Merge Sorted Array.
// Memory Usage: 2.3 MB, less than 21.74% of Go online submissions for Merge Sorted Array.
