    def maxProduct(self, a: List[int]) -> int:
        
        n = len(a)
        
        if n == 0:
            return 0
        
        if n== 1:
            return a[0]
                
        dpPos = [None] * n
        dpNeg = [None] * n
                
        for i in range(n - 1, -1, -1):

            if i == n - 1:
                if a[i] > 0:
                    dpPos[i] = a[i]
                    dpNeg[i] = 0 # need check
                    continue
                
                elif a[i] < 0:
                    dpPos[i] = 0 # need check
                    dpNeg[i] = a[i]
                
                elif a[i] == 0:
                    dpPos[i] = 0
                    dpNeg[i] = 0
            else:
                
                if a[i] > 0:
                    dpPos[i] = max(a[i] * dpPos[i + 1], a[i])
                    dpNeg[i] = min(a[i] * dpNeg[i + 1], 0)
                
                elif a[i] < 0:
                    dpPos[i] = max(a[i] * dpNeg[i + 1], 0)
                    dpNeg[i] = min(a[i] * dpPos[i + 1], a[i])
                    
                elif a[i] == 0:
                    dpPos[i] = 0
                    dpNeg[i] = 0
                    
        return max(dpPos)
