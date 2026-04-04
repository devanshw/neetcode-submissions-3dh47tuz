# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxPathSum = float("-inf")

        # checks for maxpathsum and return the max path on left or right side
        def maxPath(node):
            if not node:
                return 0 
            left = max(0, maxPath(node.left))
            right = max(0, maxPath(node.right))
            self.maxPathSum = max(self.maxPathSum, left+node.val+right)
            return max(left,right)+node.val
        
        maxPath(root)
        return self.maxPathSum