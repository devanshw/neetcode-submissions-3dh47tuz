# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if node:
                node.left, node.right = node.right, node.left
            if node and node.left:
                q.append(node.left)
            if node and node.right:
                q.append(node.right)
        return root
        
'''
BFS - process level by level
each node must swap its left and right child
for each node - do swap 
            - then push the new children to queue
continue till all nodes processed
'''