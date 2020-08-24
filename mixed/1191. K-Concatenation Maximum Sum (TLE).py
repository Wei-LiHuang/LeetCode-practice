class Solution:
    def kConcatenationMaxSum(self, a: List[int], k: int) -> int:
        
        '''
        The answer is the maximum between, 
                the answer for k=1, the sum of the whole array multiplied by k, 
            or 
                the (maximum suffix sum) + (maximum prefix sum) + (k-2) * sum(a) for k > 1. 
        '''
        def getMaxSubArrSum(arr):
            preMax, curMax = 0, 0        
            res = 0                
            n = len(arr)                        
            for i in range(n - 1, -1, -1):
                curMax = max([arr[i] + preMax, arr[i], 0])                                
                preMax = curMax
                res = max(res, curMax)                
            return res
                                
        if k == 1:
            return getMaxSubArrSum(a)
        else:
            a2 = a + a
            _subSum = getMaxSubArrSum(a2)
                
            if k == 2:
                return max([sum(a) * 2, 0, _subSum]) % (10 ** 9 + 7) 
            else:                                                                            
                return max([sum(a) * k, 0, _subSum, _subSum + sum(a) * (k - 2)]) % (10 ** 9 + 7)
                    
