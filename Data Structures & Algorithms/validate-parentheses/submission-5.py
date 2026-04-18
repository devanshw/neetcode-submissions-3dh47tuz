class Solution:
    def isValid(self, s: str) -> bool:

        closeToOpen = {"}":"{", ")":"(", "]":"["}
        stack = []
        
        for ch in s:

            if ch not in closeToOpen:
                stack.append(ch)
            else:
                if not stack or stack[-1] != closeToOpen[ch]:
                    return False
                else:
                    stack.pop()
        
        return True if not stack else False
            