class Solution:
    
    def nextGreaterElements(self, a: List[int]) -> List[int]:
        
        n = len(a)
        
        
        b = a + a
        stack = []
        m = len(b)
        
        res = [-1] * n
        for i in range(m - 1, -1, -1):
            
            while len(stack) > 0 and b[stack[-1]] <= b[i] and stack[-1] < (i + n):
                stack.pop()
        
            if i < n and len(stack) > 0:
                if b[stack[-1]] > b[i] and stack[-1] < (i + n):
                    res[i] = b[stack[-1]]
                
            stack.append(i)
                  

            
        return res[0:n]
        
