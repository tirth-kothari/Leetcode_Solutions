# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return
        res = {} 
        queue = []
        queue.append(root)
        while len(queue) > 0:
            node = queue.pop(0)
            if node.val not in res:
                res[node.val] = 1
            else:
                res[node.val] += 1
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        print(res)  
        maximum_count = max(res.values())   
        output = []
        for key, value in res.items():
            if value == maximum_count:
                output.append(key)
        return output 
