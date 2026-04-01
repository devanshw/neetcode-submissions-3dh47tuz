# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, leftB, rightB):
            if not node:
                return True
            if node.val <= leftB or node.val >= rightB:
                return False
            return dfs(node.left,leftB, node.val) and dfs(node.right, node.val, rightB)
            
        return dfs(root, float("-inf"), float("inf"))
        
        


'''
everything on left of root is smaller 
everything on right of root is bigger 
left and right subtrees are also BST 

root can be in the range(-inf to inf)
everything on left will be in range(-inf to root), right will be in (root,inf)
do this recursively till no node
if not node then just return back

'''
        