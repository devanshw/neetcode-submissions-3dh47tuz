# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        self.count = 0 

        def dfs(node, cmax):
            if not node:
                return 

            if node.val >= cmax :
                self.count += 1

            cmax = max(cmax, node.val)
            
            dfs(node.left,cmax)
            dfs(node.right,cmax)

        dfs(root,float("-inf"))
        return self.count

'''
good node - path from the root to that node contains no node greater than val of node x

start from root 
track max in that path going down 
if max <= node val then node is good 

'''
        