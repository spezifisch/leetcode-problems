# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class FunnelImage:
    def __init__(self):
        self.columns = dict()

    def add(self, val: int, row_level: int, col: int) -> None:
        column = self.columns.get(col)
        if column is None:
            self.columns[col] = { row_level: val }
        else:
            cell = column.get(row_level)
            if cell is None:
                column[row_level] = val
            else:
                if isinstance(column[row_level], int):
                    column[row_level] = [column[row_level], val]
                else:
                    column[row_level].append(val)
        
    def get_column_order(self) -> List[List[int]]:
        ret = []
        
        column_keys = sorted(self.columns.keys())
        for column_key in column_keys:
            column = self.columns[column_key]
            
            row_keys = sorted(column.keys())
            rows = []
            for k in row_keys:
                cell = column[k]
                if isinstance(cell, int):
                    rows.append(cell)
                else:
                    rows += sorted(cell)
            ret.append(rows)
        
        return ret
        
        
class Solution:
    def __init__(self):
        self.fi = FunnelImage()
    
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        stack = [(root, 0, 0)]
        while len(stack):
            node, nrow, ncol = stack.pop()
            
            self.fi.add(node.val, nrow, ncol)
            
            if node.left:
                stack.append((node.left, nrow + 1, ncol - 1))
            if node.right:
                stack.append((node.right, nrow + 1, ncol + 1))
            
        return self.fi.get_column_order()
    
# Runtime: 40 ms, faster than 71.13% of Python3 online submissions for Vertical Order Traversal of a Binary Tree.
# Memory Usage: 13.5 MB, less than 5.26% of Python3 online submissions for Vertical Order Traversal of a Binary Tree.

