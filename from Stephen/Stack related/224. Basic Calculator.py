class Solution:
    
    def calculate(self, s: str) -> int:
        
        n, stack = len(s), []
        if n == 0:
            return 0
        
        i, res = 0, 0
        
        while i < n:
            
            #print(stack)
            
            c = s[i]
            
            if c == ' ':
                i += 1
                continue                                
                
            elif c.isnumeric():
                num = ""
                while i < n and s[i].isnumeric():
                    num += s[i]
                    i += 1
                                        
                if len(stack) == 0 or stack[-1] == '(':
                    stack.append(int(num))
                    continue
                                        
                elif stack[-1] == '+':
                    stack.pop()
                    v1 = stack.pop()
                    stack.append(v1 + int(num))
                    continue
                                    
                elif stack[-1] == '-':
                    stack.pop()
                    v1 = stack.pop()
                    stack.append(v1 - int(num))
                    continue
                                                                        
            elif c == '(' or c == '+' or c == '-':
                stack.append(c)
                i += 1
                continue
                
            elif c == ')':
                val = stack.pop()
                stack.pop()#'('
                
                if len(stack) == 0:
                    stack.append(val)
                
                elif stack[-1] == '+':
                    stack.pop()
                    v1 = stack.pop()
                    stack.append(v1 + val)
                
                elif stack[-1] == '-':
                    stack.pop()
                    v1 = stack.pop()
                    stack.append(v1 - val)
                                                                                
                i += 1
                continue
        
                                                                
        return stack[-1]
