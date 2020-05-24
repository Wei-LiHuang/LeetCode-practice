class Solution:
    
    def isValid(self, S: str) -> bool:
        
        stack = []
        
        for c in S:
            
            if c == 'c':
                if len(stack) == 0 or stack[-1] != 'b':
                    return False
                else:
                    stack.pop()
                if len(stack) == 0 or stack[-1] != 'a':
                    return False
                else:
                    stack.pop()
                    
            else:
                stack.append(c)
        
        return len(stack) == 0
        
