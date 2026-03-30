# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #global variable to store running max
        self.diameter = 0
        
        def dfs(node):
            if not node:
                return 0 
            lh = dfs(node.left)
            rh = dfs(node.right)
            self.diameter = max(self.diameter, lh+rh)
            return 1 + max(lh,rh)

            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return self.diameter
            

'''
dfs 
for every node we can find the left and right ht 
then get the sum and compare with running max
'''
        