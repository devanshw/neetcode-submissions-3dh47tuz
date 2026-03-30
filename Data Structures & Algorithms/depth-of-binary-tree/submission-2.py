# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 
        stack = []
        stack.append([root,1])
        res = 0
        while stack: 
            node, nodeHt = stack.pop()
            res = max(res, nodeHt)
            if node.left:
                stack.append([node.left, nodeHt+1])
            if node.right:
                stack.append([node.right, nodeHt+1])
        return res



'''
iterative DFS with a stack 
we can store the (node, curHt) in the stack
for every pop 
    update the maximum depth seen so far 
    push children with depth + 1
'''
        