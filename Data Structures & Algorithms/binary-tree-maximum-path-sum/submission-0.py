# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        # helper func find the max path from a node 
        def getMaxPath(node):
            if not node:
                return 0 

            left = getMaxPath(node.left)
            right = getMaxPath(node.right)

            totalPath = node.val + max(left,right)

            return totalPath if totalPath>0 else 0

        self.res = -float("inf")
        def dfs(node):
            if not node:
                return 
            
            left = getMaxPath(node.left)
            right = getMaxPath(node.right)

            self.res = max(self.res,   node.val + left + right)

            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return self.res

        
        