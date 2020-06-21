class Solution:
    
    def asteroidCollision(self, a: List[int]) -> List[int]:        
        n = len(a)
        stack = []        
        for i in range(0, n):            

            if a[i] > 0:
                stack.append(a[i])
                
            elif a[i] < 0:                
                if len(stack) == 0 or stack[-1] < 0:
                    stack.append(a[i])
                else:
                    while len(stack) > 0  and stack[-1] > 0:                    
                        if abs(a[i]) > stack[-1]:
                            stack.pop()                                                        
                        elif abs(a[i]) == stack[-1]:
                            a[i] = 0
                            stack.pop()
                            break
                        elif abs(a[i]) < stack[-1]:
                            a[i] = 0
                            break
                    if a[i] != 0:
                        stack.append(a[i])
                    
        return stack
