# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.res = float("-inf")

        def maxPath(node):
            if not node:
                return 0 
            
            left = max(0, maxPath(node.left))
            right = max(0, maxPath(node.right))

            self.res = max(self.res, node.val + left + right)

            return node.val + max(left,right)
        
        maxPath(root)

        return self.res
        