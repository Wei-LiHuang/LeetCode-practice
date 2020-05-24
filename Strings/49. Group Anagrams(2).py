# not sure about the solution at start
# sort each str => O(W logW), w is the length of each words -> O(N * W log W) or counting sort O(N*W)
# turn each word into count char list: each list length is fixed:26 -> need O(W) to turn to list
# but lst can't hash -> turn to str then use hash map


class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        _dict = {}                
        
        keySet = []
        for w in strs:
            
            w2 = str(sorted(w))
            
            if w2 in _dict:
                _dict[w2].append(w)            
            else:
                _dict[w2] = [w]
                keySet.append(w2)
        
        
        res = []
        for key in keySet:
            res.append(_dict[key])
            
        return res
        
        
        
