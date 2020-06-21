# brute: find the biggest element in l ~ r, m
# if m == r, r -= 1,  continue
# flip l ~ m, flip l ~ r, r -= 1 ---> finding max amkes O(N^2)

# how to reach O(N) ?

class Solution:
    def pancakeSort(self, a: List[int]) -> List[int]:
        
        def flip(a, l, r):
            while l < r:                
                a[l], a[r] = a[r], a[l]
                l += 1
                r -= 1
                
        def findMax(a, l, r):
            _max = -float('inf')
            m = -1
            for i in range(l, r + 1):
                if a[i] > _max:
                    m = i
                    _max = a[i]
            return m
        
        
        n = len(a)
        res = []
        l, r = 0, n - 1
        while l < r:
            m = findMax(a, l, r)
            if m == r:
                r -= 1
            else:
                flip(a, l, m)
                res.append(m - l + 1)
                flip(a, l, r)
                res.append(r - l + 1)
                r -= 1
                            
        return res
