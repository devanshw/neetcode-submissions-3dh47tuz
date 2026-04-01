# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        self.counter = k 

        def inorder(node):
            if not node:
                return 
            inorder(node.left)

            self.counter -= 1
            if self.counter == 0:
                self.res = node.val
                return

            inorder(node.right)

        inorder(root)
        return self.res
            
            
        

'''
BST - left is smaller, right is bigger
we need to find the kth smallest 

the smallest would be the left most 
then parent of left most 
then right child child of parent 

this is same as left node right which is inorder traversal 
we can keep traversing inorder and decrement k for each node seen 
once k reaches 0 we have seen the kth smallest 
return the last element seen
'''