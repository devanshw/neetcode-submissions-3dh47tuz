# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def getHt(node):
            if not node:
                return 0
            lh = getHt(node.left)
            rh = getHt(node.right)
            return 1 + max(lh,rh)
        
        return getHt(root)

'''
dfs - depth first 
height func that takes in a node 
we get the height of both the childs and check which is more 
add one to that for the current and return 
'''
        