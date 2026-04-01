# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if not preorder or not inorder:
            return None 

        root = TreeNode(preorder[0]) 
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root

'''
given preorder and postorder traversal 
preorder - left node right
postorder - left right node

first element of preorder gives the root 
find the position of this element in inorder 
eveything on left of that inorder comes in left subtree, right comes 

finish when either of the list ends

'''
        