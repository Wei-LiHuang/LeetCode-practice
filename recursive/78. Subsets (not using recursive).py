# start = n -> res: []
# start = n - 1 -> res: [] + a[n - 1] -> res = [[], [a[n - 1]]]
# start = n - 2 -> res: [] + a[n - 2], [a[n - 1]] + a[n - 2], []
# start = n - 3 -> res: [] + a[n - 3], [a[n - 2], a[n - 3]], [a[n - 1], a[n - 2], a[n - 3]] + ...

class Solution:
    
    def subsets(self, a: List[int]) -> List[List[int]]:
        
        n, res = len(a), [[]]
                
        for i in range(n - 1, -1, -1):       
            size = len(res)
            for j in range(0, size):
                res.append(res[j] + [a[i]])
        
        return res
        
            
            
            
        
