class Solution:
    def maxAbsValExpr(self, x: List[int], y: List[int]) -> int:                                
        '''
            straight forward: O(N^2) -> TLE
            n = len(arr1)

            _max = 0
            for i in range(0, n):
                for j in range(i, n):
                    _max = max(_max, abs(arr1[i] - arr1[j]) + abs(arr2[i] - arr2[j]) + abs(i - j))

            return _max
        '''     
        
        '''
            |arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|
            
            => dis(p1, p2) + |i - j|
            
            assume i <= j:
                |x[i] - x[j]| = (x[i] - x[j]), (-x[i] + x[j]) 
                |y[i] - y[j]| = (y[i] - y[j]), (-y[i] + y[j])
                |i - j| = j - i
                
                (x[i] - x[j]) + (y[i] - y[j]) + (j - i)
                -> (x[i] + y[i] - i) - (x[j] + y[j] - j) 
                                                            -> f(i) - f(j), f(i) = x[i] + y[i] - i
                (x[i] - x[j]) + (-y[i] + y[j]) + (j - i)
                -> (x[i] - y[i] - i) - (x[j] - y[j] - j)    
                                                            -> f(i) - f(j), f(i) = x[i] - y[i] - i                                
                (-x[i] + x[j]) + (y[i] - y[j]) + (j - i)
                -x[i] + y[i] - i + x[j] - y[j] + j          
                                                            -> f(i) - f(j), f(i) = -x[i] + y[i] - i        
                (-x[i] + x[j]) + (-y[i] + y[j]) + (j - i)
                -x[i] - y[i] - i + x[j] + y[j] + j          
                                                            -> f(i) - f(j), f(i) = -x[i] - y[i] - i
                
                
                f(i) = p * x[i] + q * y[i] - i, p = +- 1, q = +- 1
                
                find the max of f(i) - f(j), where j >= i
        '''        
        #1. find the smallest f(i) and max f(i):
        n, _max = len(x), -float('inf')        
        for p, q in [[1, -1], [-1, 1], [1, 1], [-1, -1]]:            
            # need reset the min every time we change p, q:
            _min = float('inf')
            # i from n - 1 to 0, used i store the min val as the min f(j), j > i
            for i in range(n - 1, -1, -1):
                fi = p * x[i] + q * y[i] - i
                _min = min(fi, _min)
                _max = max(fi - _min, _max)
                
        return _max
