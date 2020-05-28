#recursion solution:

class Solution:
    
    def twoSum(self, a: List[int], tgt: int) -> List[int]:
        
        def rec (start, a, tgt, _map):
                                    
            cur = a[start]
            if cur in _map:                
                return [_map[cur], start]
            else:
                _map[tgt - cur] = start
            
            return rec(start + 1, a, tgt, _map)
        
        _map = {}
        
        return rec(0, a, tgt, _map)
            
            
