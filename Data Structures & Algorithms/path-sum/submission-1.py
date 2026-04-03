# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(node, csum):
            if not node:
                return False 

            csum += node.val

            if not node.left and not node.right:
                if csum == targetSum:
                    return True
            
            return dfs(node.left, csum) or dfs(node.right, csum)

        
        return dfs(root,0)

        