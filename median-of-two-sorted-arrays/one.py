class Solution:
    def next(self):
        a = b = None
        try:
            a = self.nums1[self.pos1]
        except IndexError:
            pass
        try:
            b = self.nums2[self.pos2]
        except IndexError:
            pass
        
        use_a = use_b = False
        
        if a is not None and b is None:
            use_a = True
        elif b is not None and a is None:
            use_b = True
        elif a <= b:
            use_a = True
        else:
            use_b = True
            
        if not use_a and not use_b:
            return None
        
        if use_a:
            self.pos1 += 1
            return a
        else:
            self.pos2 += 1
            return b
        
        raise RuntimeError()
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        self.nums1 = nums1
        self.pos1 = 0
        self.nums2 = nums2
        self.pos2 = 0
        
        len1 = len(nums1)
        len2 = len(nums2)
        total_len = len1 + len2
        total_len_even = (total_len % 2) == 0
        
        if total_len_even:
            wanted_idx_a = int(total_len / 2) - 1
            wanted_idx_b = wanted_idx_a + 1
        else:
            wanted_idx_a = int(total_len / 2)
            wanted_idx_b = None
        
        wanted_values = []
        
        idx = 0
        while True:
            value = self.next()
            #print(value)
            if value is None:
                break
            
            if idx == wanted_idx_a:
                wanted_values.append(value)
                
                if not total_len_even:
                    break
            elif idx == wanted_idx_b:
                wanted_values.append(value)
                break
            
            idx += 1
        
        if total_len_even:
            return sum(wanted_values) / 2
        
        return wanted_values[0]
        
# Runtime: 108 ms, faster than 49.96% of Python3 online submissions for Median of Two Sorted Arrays.
# Memory Usage: 13.4 MB, less than 5.11% of Python3 online submissions for Median of Two Sorted Arrays.

