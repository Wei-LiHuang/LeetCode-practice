class Solution:
    
    def coinChange(self, a: List[int], tgt: int) -> int:
        
        def getNextStep(a, tgt, curAmount, cointCount, memo):
            
            res = []
            
            newCoinCount = cointCount + 1
            for i in range(0, len(a)):                
                newAmount = curAmount + a[i]         
                if newAmount <= tgt and newAmount not in memo:
                        memo.add(newAmount)
                        res.append(newAmount)
                        if newAmount == tgt:
                            break
                        
            return res
                    
        cointCount, lst, memo = 0, [], set()
        
        lst.append(0)
        
        while len(lst) > 0:
            curSize = len(lst)
            nlst = []
            
            for i in range(0, curSize):
                cur = lst.pop()
                if cur == tgt:
                    return cointCount                
                nextSteps = getNextStep(a, tgt, cur, cointCount, memo)                                
                nlst.extend(nextSteps)
                
            lst = nlst
            cointCount += 1
                        
        return -1
                
