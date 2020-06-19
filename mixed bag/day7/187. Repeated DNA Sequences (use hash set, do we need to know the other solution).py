class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        n = len(s)
        _set = set()
        res = set()
        
        for i in range(0, n):            
            subStr = ""
            if i + 10 <= n:
                subStr = s[i : i + 10]            
            else:
                break
            
            if subStr != "":
                if subStr in _set and subStr not in res:
                    res.add(subStr)
                else:
                    _set.add(subStr)
                
        return res
