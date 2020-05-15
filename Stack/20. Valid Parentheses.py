class Solution(object):
    
    def isValid(self, s):
        
        stack = []
        
        for c in s:
            
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                
                if len(stack) == 0:
                    return False
                
                if c == ')':
                    if stack[-1] != '(':
                        return False
                    else:
                        stack.pop()
                if c == '}':
                    if stack[-1] != '{':
                        return False
                    else:
                        stack.pop()   
                if c == ']':
                    if stack[-1] != '[':
                        return False
                    else:
                        stack.pop()                
            
        
        if len(stack) == 0:
            return True
        
        return False
