class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        content_children = 0
        next_cookie_idx = 0
        for child_greed in g:
            for idx, cookie_size in enumerate(s[next_cookie_idx:], next_cookie_idx):
                if cookie_size >= child_greed:
                    next_cookie_idx = idx + 1
                    content_children += 1
                    break
                    
        return content_children
    
# Runtime: 552 ms, faster than 10.54% of Python3 online submissions for Assign Cookies.
# Memory Usage: 14.5 MB, less than 5.09% of Python3 online submissions for Assign Cookies.

