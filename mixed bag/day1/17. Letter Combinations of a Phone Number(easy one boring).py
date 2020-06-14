#boring question

class Solution:
    
    def letterCombinations(self, digits: str) -> List[str]:
        
        _dict = {'2': ['a','b','c'], '3': ['d','e','f'], '4': ['g','h','i'], '5': ['j','k','l'], 
                   '6': ['m','n','o'], '7': ['p','q','r','s'], '8': ['t','u','v'], '9': ['w','x','y','z']}
        
        res = []
        for d in digits:                        
            arr = _dict[d]
            r = []
            for c in arr:
                if len(res) == 0:
                    r.append(str(c))
                else:
                    for x in res:
                        _str = x + str(c)
                        r.append(_str)
            
            res = r
        
        
        return res
            
