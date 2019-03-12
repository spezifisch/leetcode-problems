"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        porder = []
        stack = []
        node = root
        while True:
            if not len(node.children):
                porder.append(node.val)
                
                if node == root:
                    break
                
                node = stack.pop()
                continue
        
            stack.append(node)
            node = node.children.pop(0)
            
        return porder
            
# Runtime: 120 ms, faster than 6.84% of Python3 online submissions for N-ary Tree Postorder Traversal.
# Memory Usage: 17.8 MB, less than 6.03% of Python3 online submissions for N-ary Tree Postorder Traversal.

