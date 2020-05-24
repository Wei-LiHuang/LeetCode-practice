# cmp: item getter

class Solution:
    
    def merge(self, a: List[List[int]]) -> List[List[int]]:
                
        a = sorted(a, key=itemgetter(0))
        
        res = []
        
        for p in a:
            
            if len(res) == 0:
                res.append(p)
                continue
            
            if p[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], p[1])
            else:
                res.append(p)
                
        return res
        
