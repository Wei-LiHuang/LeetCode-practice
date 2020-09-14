class Solution:
    def maxEqualRowsAfterFlips(self, a: List[List[int]]) -> int:
        
        d = dict()
        
        for i in range(0, len(a)):
            p = dict()
            p[a[i][0]] = 'A'
            pattern = []
            for j in range(0, len(a[0])):
                if a[i][j] in p:
                    pattern.append('A')
                else:
                    pattern.append('B')
            
            _str = ''.join(pattern)
            if _str in d:
                d[_str] += 1
            else:
                d[_str] = 1
                
        #print(d)
        
        _max = 0
        for val in d.values():
            _max = max(_max, val)
        
        
        return _max
            
