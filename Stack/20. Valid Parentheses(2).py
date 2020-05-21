class Solution(object):
    
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True        
        stack = []

        for c in s:
            
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                
                if not stack:
                    return False
                
                if c == ')':
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                if c == ']':
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
                    
                if c == '}':
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
                            
        return len(stack) == 0
        
