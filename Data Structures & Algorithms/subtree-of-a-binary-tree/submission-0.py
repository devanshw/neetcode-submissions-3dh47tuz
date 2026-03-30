# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sameTree(n1, n2):
            if not n1 and not n2:
                return True
            elif not n1 or not n2:
                return False 
            elif n1.val != n2.val:
                return False 
            
            return sameTree(n1.left, n2.left) and sameTree(n1.right, n2.right)
        
        def checkSubTree(big,small):
            if not big:
                return False 
            if sameTree(big,small):
                return True
            return checkSubTree(big.right, small) or checkSubTree(big.left,small)

        return checkSubTree(root,subRoot)


'''
we can use the same tree func to check if the any node is same as the root of subtree 
'''
        