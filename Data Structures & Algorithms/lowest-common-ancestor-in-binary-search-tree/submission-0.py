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

        # if the min(p,q) > root go right
        if min(p.val, q.val) > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        # if max(p,q) < root go left
        elif max(p.val, q.val) < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root

        

'''
LCA - lowest common ancestor
lca of p and q is the lowest node in a Tree with both p and q as desendants 

BST - values on right are bigger, left are smaller

we are given p and q values 
if both are smaller than cur node - both must lie on the left subtree
if both bigger - both must lie on the right subtree
otherwise we are at a split point where one node is a left child / right child 
the split point is the LCA


'''
        