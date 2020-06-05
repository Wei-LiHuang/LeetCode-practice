"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, a: List['Employee'], id: int) -> int:
        
        
        def dfs(_map, id, res):            
            
            for s in _map[id][1]:
                dfs(_map, s, res)
            
            res[0] += _map[id][0]
            
            return
            
        
        
        _map = dict()
        for emplyeeData in a:
            _map[emplyeeData.id] = [emplyeeData.importance, emplyeeData.subordinates]
        
        res = [0]        
        dfs(_map, id, res)
        
        return res[0]
