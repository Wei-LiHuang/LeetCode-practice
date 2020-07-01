    def fourSum(self, a: List[int], tgt: int):
        
        def twoSum(a, l, tgt, parent):
            n = len(a)
            
            r = n - 1
            
            if tgt < sum([a[l], a[l]]):
                return []            
            if tgt > sum([a[r], a[r]]):
                return []         
            
            res = []
            while l < r:
                _sum = a[l] + a[r]
                if _sum == tgt:
                    lst = list(parent)
                    lst.extend([a[l],a[r]])                                  
                    res.append(lst)           
                    
                    l += 1
                    while l <= n - 1 and a[l] == a[l - 1]:
                        l += 1                        
                    r -= 1
                    
                    while r >= 0 and a[r] == a[r + 1]:
                        r -= 1
                        
                elif _sum < tgt:
                    l += 1
                elif _sum > tgt:
                    r -= 1
                    
            return res
        
        def N_Sum(a, l, tgt, parent, nSum):            
            res = []
            n = len(a)
            for i in range(l, n - nSum + 1):
                if i > l and a[i] == a[i - 1]:
                    continue                    
                parent.append(a[i])
                if nSum == 3:
                    nextRes = twoSum(a, i + 1, tgt - a[i], parent)
                else:                   
                    nextRes = N_Sum(a, i + 1, tgt - a[i], parent, nSum - 1)
                parent.pop()
                
                res.extend(nextRes)                           
            return res        
        
        a.sort()
        res = N_Sum(a, 0, tgt, [], 4)
        return res
