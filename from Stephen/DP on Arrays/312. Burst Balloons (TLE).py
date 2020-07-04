# from top to bot: l = n -> l = 0.
class Solution:
    
    def maxCoins(self, a: List[int]) -> int:
        
        def indexSeqToString(curSeq):
            return str(curSeq)
                    
        # curSeq: index left -> at first is [0, 1, 2, ..., n - 1]
        def rec(a, curSeq, curCount, res, memo):          
            l = len(a)
            
            # if all balloon bursted:
            if len(curSeq) == 0:
                res[0] = max(res[0], curCount)
                return
            
            _str = indexSeqToString(curSeq)
            if _str in memo and memo[_str] > curCount:
                return
                                                    
            n = len(curSeq)
            
            if n == 1:
                rec(a, [], curCount + a[curSeq[0]], res, memo)
            
            elif n == 2:
                newCount = curCount + a[curSeq[0]] * a[curSeq[1]]
                rec(a, [curSeq[0]], newCount, res, memo)
                if a[curSeq[0]] !=a[curSeq[1]]:
                    rec(a, [curSeq[1]], newCount, res, memo)
            
            else:
                # still get ballons:
                for i in range(0, n):
                    if i == 0:
                        newCount = curCount + 1 * a[curSeq[i]] * a[curSeq[i + 1]]
                        newSeq = curSeq[1 : n]
                        rec(a, newSeq, newCount, res, memo)                    

                    elif i == n - 1:
                        newCount = curCount + a[curSeq[i - 1]] * a[curSeq[i]] * 1
                        newSeq = curSeq[0 : i]                        
                        rec(a, newSeq, newCount, res, memo)

                    else:
                        newCount = curCount + a[curSeq[i - 1]] * a[curSeq[i]] * a[curSeq[i + 1]]
                        newSeq = curSeq[0 : i] + curSeq[i + 1 : n]
                        rec(a, newSeq, newCount, res, memo)
                                

            memo[_str] = curCount            
            return
        
        
        n = len(a)
        indexSeq = []
        for i in range(0, n):
            indexSeq.append(i)
                
        memo = dict()
        
        res = [0]
        rec(a, indexSeq, 0, res, memo)
        
        return res[0]
