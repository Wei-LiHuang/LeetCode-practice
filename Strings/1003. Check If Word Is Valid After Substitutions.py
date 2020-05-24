#abc abc ab ab abc c



class Solution:
    
    def isValid(self, S: str) -> bool:
        
        stack = []
        
        n = len(S)
        
        for i in range(0, n):
            
            cur = S[i]
            
            #check pop:
            if cur == 'c':
                if len(stack) >= 2 and stack[-1] == 'b' and stack[-2] == 'a':
                    stack.pop()
                    stack.pop()
                else:
                    stack.append(cur)
            else:
                stack.append(cur)
            
        return len(stack) == 0
            
            
        
        
        
