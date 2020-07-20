class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        
        def toOrderTuple(s):
            order = []
            _min = float('inf')
                        
            for i in range(1, len(s)):
                o = ord(s[i]) - ord(s[i - 1])
                if o < 0:
                    o += 26
                order.append(o)               
                
            return tuple(order)        
        
        
        d = dict()
        for s in strings:
            t = toOrderTuple(s)
            if t in d:
                d[t].append(s)
            else:
                d[t] = [s]
        
        res = []
        for val in d.values():
            res.append(val)
            
        return res
        
