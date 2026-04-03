# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        self.found = False

        def dfs(node, csum):
            if not node:
                return False 

            csum += node.val

            if not node.left and not node.right:
                if csum == targetSum:
                    self.found = True
                    return 
            
            dfs(node.left, csum)
            dfs(node.right, csum)

            return False

        dfs(root,0)
        return self.found

        