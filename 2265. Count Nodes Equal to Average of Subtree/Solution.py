# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root):
        return self.explore(root)[2]

    def explore(self, node):
        #Given a node, returns the following tuple:
        #(numNodesBeneath, sumOfNodesBeneath, numNodesThatAreTheirAverage)
        if node == None:
            return (0, 0, 0)
        left, right = self.explore(node.left), self.explore(node.right)
        totNum = left[0] + right[0] + 1
        totSum = left[1] + right[1] + node.val
        totAvg = left[2] + right[2]
        if totSum // totNum == node.val:
            totAvg += 1
        return (totNum, totSum, totAvg)
