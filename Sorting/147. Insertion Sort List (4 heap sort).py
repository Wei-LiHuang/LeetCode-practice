class Solution:
    
    def sortArray(self, a: List[int]) -> List[int]:
                
        def heapify(a, i, end):
            l, r = i * 2 + 1, i * 2 + 2
            
            _min = i
            if l < end and a[l] < a[i]:
                _min = l
            if r < end and a[r] < a[_min]:
                _min = r
                
            if _min != i:
                a[_min], a[i] = a[i], a[_min]                
                heapify(a, _min, end)
            return                    
        
        n = len(a)
        for i in range(n - 1, -1, -1):
            heapify(a, i, n)
        
        res = []
        for i in range(0, n):
            res.append(a[0])
            a[0], a[n - i - 1] = a[n - 1 - i], a[0]
            heapify(a, 0, n - i - 1)
                            
        return res
            
        
