import collections

class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        columns = collections.defaultdict(lambda: [])
        for row_idx, row in enumerate(A):
            for col_idx, letter in enumerate(row):
                columns[col_idx].append(letter)
        
        deletion_count = 0
        for col_idx, column in columns.items():
            if sorted(column) != column:
                # it's not sorted, so it should be deleted
                deletion_count += 1
        
        return deletion_count
        
# Runtime: 268 ms, faster than 16.06% of Python3 online submissions for Delete Columns to Make Sorted.
# Memory Usage: 14.8 MB, less than 5.45% of Python3 online submissions for Delete Columns to Make Sorted.

