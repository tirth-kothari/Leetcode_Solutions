# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node, min_, max_):
            if not node:
                self.result = max(self.result, abs(min_ - max_))
                return 
            
            min_ = min(min_, node.val)
            max_ = max(max_, node.val)            
            dfs(node.left, min_, max_)
            dfs(node.right, min_, max_)            
            
        self.result = 0
        dfs(root, root.val, root.val)
        
        return self.result
