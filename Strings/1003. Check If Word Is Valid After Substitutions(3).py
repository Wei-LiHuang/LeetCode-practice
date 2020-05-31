class Solution:
    
    def isValid(self, s: str) -> bool:
        
        n, stack = len(s), []
        for i in range(0, n):
            c = s[i]
            if c == 'a' or c == 'b':
                stack.append(c)
            if c == 'c':                
                if len(stack) < 2:
                    return False
                else:
                    if stack[-1] != 'b' or stack[-2] != 'a':
                        return False
                    stack.pop()
                    stack.pop()
        
        return len(stack) == 0
                    
            
            
        
