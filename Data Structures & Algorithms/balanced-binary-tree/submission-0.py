# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node:
                return 0
            lh = dfs(node.left)
            if lh == -1:
                return -1
            rh = dfs(node.right)
            if rh == -1:
                return -1
            
            if (abs(lh-rh) > 1):
                return -1

            return 1 + max(lh,rh)
        
        if not root:
            return True
        res = dfs(root)
        return False if res == -1 else True
            

'''
dfs 
get left and right ht then check for imbalance 
if imbalanced return -1 
next time if func is returned on lh/ rh we know there is imbalance on that side so return -1
'''