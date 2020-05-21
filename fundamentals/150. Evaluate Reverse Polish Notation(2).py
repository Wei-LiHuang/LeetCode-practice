class Solution(object):
    def evalRPN(self, tokens):
        
        stack = []
        
        for t in tokens:
            
            try: 
                stack.append(int(t))            
            except:
                v2 = stack[-1]
                stack.pop()
                v1 = stack[-1]
                stack.pop()                
                
                if t == "+":
                    stack.append(v1 + v2)                                        
                if t == "-":
                    stack.append(v1 - v2)                        
                if t == "*":
                    stack.append(v1 * v2)                        
                if t == "/":
                    stack.append(int(float(v1) / v2))
                    
        return stack[0]
