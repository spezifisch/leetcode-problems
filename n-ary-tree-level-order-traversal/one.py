"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        self.levels = []
        self.levelOrderRecurse(root, depth=0)
        return self.levels
        
    def levelOrderRecurse(self, root: 'Node', depth: int) -> None:
        if not root:
            return
        
        if depth >= len(self.levels):
            self.levels.append([root.val])
        else:            
            self.levels[depth].append(root.val)
        
        for child in root.children:
            self.levelOrderRecurse(child, depth + 1)
            
# Runtime: 104 ms, faster than 45.12% of Python3 online submissions for N-ary Tree Level Order Traversal.
# Memory Usage: 17.6 MB, less than 5.47% of Python3 online submissions for N-ary Tree Level Order Traversal.

