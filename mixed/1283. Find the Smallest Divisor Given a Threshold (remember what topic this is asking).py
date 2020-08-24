class Solution:
    def smallestDivisor(self, a: List[int], threshold: int) -> int:
        
        '''
            a = [1,2,5,9], [divisor, sum] ->
            [[17, 4], [16, 4], [15, 4], [14, 4], [13, 4], [12, 4], [11, 4], [10, 4], [9, 4], [8, 5], [7, 5], [6, 5], [5, 5], [4, 7], [3, 7], [2, 10], [1, 17]]       
        '''
        
        def getSum(a, d, memo):
            
            if d in memo:
                return memo[d]
            
            res = 0
            for v in a:
                if (v // d) == v / d:
                    res += v // d 
                else:
                    res += (v // d) + 1
                    
            memo[d] = res
            return res
        
        memo = dict()        
        minD, maxD = 1, max(a)
        
        while minD <= maxD:
            
            if minD == maxD:
                return minD            
            else:
                mid = (minD + maxD) // 2
                _sum = getSum(a, mid, memo)
                
                if _sum > threshold:
                    minD = mid + 1
                else:
                    maxD = mid
                                        
        return 0
