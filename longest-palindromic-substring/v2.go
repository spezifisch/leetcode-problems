package v2

type State struct {
	Input                                string
	LongestStart, LongestEnd, LongestLen int
}

func (s *State) CheckPalindrome(startIdx, endIdx int) {
	if s.IsPalindrome(startIdx, endIdx) {
		thisLen := endIdx - startIdx + 1
		if thisLen > s.LongestLen {
			s.LongestLen = thisLen
			s.LongestStart = startIdx
			s.LongestEnd = endIdx
		}
	}
}

func (s *State) IsPalindrome(startIdx, endIdx int) bool {
	if startIdx >= endIdx {
		return true
	}
	if s.Input[startIdx] != s.Input[endIdx] {
		return false
	}
	return s.IsPalindrome(startIdx+1, endIdx-1)
}

func longestPalindrome(s string) string {
	state := State{
		Input: s,
	}

	for startIdx := range s {
		for endIdx := startIdx + 1; endIdx < len(s); endIdx++ {
			state.CheckPalindrome(startIdx, endIdx)
		}
	}

	return s[state.LongestStart : state.LongestEnd+1]
}

// Runtime: 2660 ms, faster than 5.04% of Go online submissions for Longest Palindromic Substring.
// Memory Usage: 2.7 MB, less than 38.59% of Go online submissions for Longest Palindromic Substring.
// oof...
