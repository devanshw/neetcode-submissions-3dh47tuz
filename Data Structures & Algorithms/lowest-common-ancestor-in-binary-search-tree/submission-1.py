# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        if not root or not p or not q:
            return None 
        
        if max(p.val, q.val) < root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        
        elif min(p.val, q.val) > root.val:
            return self.lowestCommonAncestor(root.right,p,q)

        else:
            return root

        

'''
given tree is BST 
everything on right is bigger, everything on left is smaller 
we are given root, p , q 
if the 2 nodes p,q's maximum is less than root 
means both are smaller than root -- search on the left 

if the 2 nodes p,q's minimum is more than root 
means both are larger than root -- search on the right

if one of the 2 is the same as root - thats a pivot value so ans in the root
'''