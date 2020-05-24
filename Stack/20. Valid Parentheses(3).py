class Solution:
    
    def isValid(self, s: str) -> bool:
        
        d = {}
        
        d['('] = ')'
        d['{'] = '}'
        d['['] = ']'
        
        stack = []
        for c in s:
            
            if c in d:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                
                if d[stack[-1]] == c:
                    stack.pop()
                else:
                    return False                    

        
        return len(stack) == 0
            
            
