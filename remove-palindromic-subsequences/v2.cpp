class Solution {
 public:
  int removePalindromeSub(string s) {
    int a = 0, b = s.size() - 1;
    while (a < b) {
      if (s[a] != s[b]) {
        return 2;
      }
      a++;
      b--;
    }
    return 1;
  }
};

// Runtime: 3 ms, faster than 38.93% of C++ online submissions for Remove
// Palindromic Subsequences. Memory Usage: 6.1 MB, less than 79.13% of C++
// online submissions for Remove Palindromic Subsequences.
