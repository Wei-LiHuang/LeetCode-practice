class Solution:
    
    def grayCode(self, n: int) -> List[int]:
        
        def toVal(code):
            n = len(code)
            p, val = 1, 0            
            for i in range(n - 1, -1, -1):
                val += (code[i] * p)
                p *= 2
                
            return val
                                    
        if n == 0:
            return [0]
                
        bits = [0, 1]
        code = [[0], [1]]
                
        for i in range(1, n):                        
            nextCode = []
            
            for j in range(0, len(code)):
                
                if j % 2 == 0:      
                    code[j].append(0)
                    nextCode.append(list(code[j]))
                    code[j].pop()
                    
                    code[j].append(1)
                    nextCode.append(list(code[j]))
                    code[j].pop()
                else:
                    code[j].append(1)
                    nextCode.append(list(code[j]))
                    code[j].pop()
                    
                    code[j].append(0)
                    nextCode.append(list(code[j]))
                    code[j].pop()
                    
            code = nextCode
            
            
        res = []
        for c in code:
            res.append(toVal(c))
            
        
        return res
