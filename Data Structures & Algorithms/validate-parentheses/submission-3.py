class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {"}":"{", "]":"[", ")":"("} 
        stack = []
        for p in s:
            #push open paras
            if p not in closeToOpen:
                stack.append(p)
            else:
                if not stack or stack[-1] != closeToOpen[p]:
                    return False
                else:
                    stack.pop() 
        return True if not stack else False
        
'''
stack to track first in last out as the first para open will be the last to get closed 
have a maping for open - close relation 
close to open is better as we can push the open paras to stack and then if we encounter a closing para 
we pop from stack and check if the mapping is same 
'''