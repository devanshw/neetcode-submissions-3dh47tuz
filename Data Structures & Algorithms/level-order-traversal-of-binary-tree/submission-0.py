# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q.append(root)
        res = []

        while q:
            qlen = len(q)
            level = [] 
            for _ in range(qlen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return res
            
                


'''
bredth first - level order 
need to visit all nodes on the level then move down 
queue - first in last first out 
start with root
queue = [root]
find how many elements in cur level - qlen 
for qlen times get elements from left and push in a result array 
and insert left and right child if any 
'''
        