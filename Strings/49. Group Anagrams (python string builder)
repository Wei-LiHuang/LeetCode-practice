# not sure about the solution at start
# sort each str => O(W logW), w is the length of each words -> O(N * W log W) or counting sort O(N*W)
# turn each word into count char list: each list length is fixed:26 -> need O(W) to turn to list
# but lst can't hash -> turn to str then use hash map


class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        _dict = {}
        
        for w in strs:
            
            arr = [0] * 26            
            for c in w:
                index = ord(c) - ord('a')
                arr[index] += 1
            
            sortedStr = ""
            for v in arr:
                sortedStr += (str(v) + "|")
            
            if sortedStr in _dict:
                _dict[sortedStr].append(w)
            else:
                _dict[sortedStr] = [w]
            
            
        res = []
        for val in _dict.values():
            res.append(val)
        
        return res
            
            
        
        
        
