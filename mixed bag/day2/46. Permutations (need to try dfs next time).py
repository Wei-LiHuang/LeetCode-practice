# reduce the length: n = 4 -> n = 3 -> n = 2 -> pass
# Ryan: dfs() -> try this next time

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def twoElement(_input):
            v1, v2 = _input[0], _input[1]
            if v1 == v2:
                return [[v1, v1]]            
            return [[v1, v2],[v2, v1]]
        
        def N_Element(_input):                            
            _len = len(_input)
            
            if _len == 2:
                return twoElement(_input)
            
            res = []
            for i in range(0, _len):                
                subList = _input[0: i]
                subList.extend(_input[(i + 1):])
                subPer = N_Element(subList)
                
                for s in subPer:
                    s.append(_input[i])
                
                res.extend(subPer)  
                    
            return res
                
        if len(nums) <= 1:
            return [nums]
        
        res = N_Element(nums)
        
        return res
                
                
            
            
        
