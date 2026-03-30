# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node):
            if not node:
                return 
            node.left, node.right = node.right, node.left
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return root
    
'''
dfs - depth first 
dfs function that takes in a node and replaces both its child 
then run on both the children 
base case would be if there is no node then we can just return 
'''
        