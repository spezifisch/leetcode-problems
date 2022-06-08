package v1

func removePalindromeSub(s string) int {
	a := 0
	b := len(s) - 1

	// check if the whole string is a palindrome
	for a < b {
		if s[a] != s[b] {
			// the whole string is not a palindrome.
			// the trick is you can always remove all "a"s in the first step
			// and all the "b"s in the second step. therefore the answer is always 2 in this case.
			return 2
		}
		a++
		b--
	}

	// it's a palindrome so we can make it empty in one step
	return 1
}

// Runtime: 0 ms, faster than 100.00% of Go online submissions for Remove Palindromic Subsequences.
// Memory Usage: 1.9 MB, less than 33.33% of Go online submissions for Remove Palindromic Subsequences.
