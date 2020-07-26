class Solution:
    
    def maxScore(self, a: List[int], k: int) -> int:        
        
        '''
            cardPoints = [1,2,3,4,5,6,1]
                -> 1, [1,2,3,4,5,6] -> 1 + 6, [1,2,3,4,5] -> 1 + 6 + 5, [1,2,3,4]                
            find the max from sides = find the min in between
            -> find the length = (n - k) subsequence which has the min sum
        '''        
        total = sum(a)
        n = len(a)
        if k >= n:
            return total
                
        _sum = sum(a[0: n - k])
        minSum = _sum        
        for i in range(0, k):
            _sum -= a[i]            
            _sum += a[i + n - k]                        
            minSum = min(minSum, _sum)
            
        return total - minSum
            
