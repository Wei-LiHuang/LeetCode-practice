# need to be careful to the division

class Solution(object):
                
    def evalRPN(self, tokens):
        
        res = 0
        stack = []
                
        for c in tokens:
            
            try:
                stack.append(int(c))
            except:
                n2 = stack[-1]
                stack.pop()
                n1 = stack[-1]
                stack.pop()
                                
                if c == "+":
                    stack.append(n1 + n2)
                if c == "-":
                    stack.append(n1 - n2)
                if c == "*":
                    stack.append(n1 * n2)
                if c == "/":                    
                     stack.append(int(float(n1)/n2))
        
        res = stack[-1]
                    

        return res
        
