# not sure about the solution at start
# sort each str => O(W logW), w is the length of each words -> O(N * W log W) or counting sort O(N*W)
# turn each word into count char list: each list length is fixed:26 -> need O(W) to turn to list
# but lst can't hash -> turn to str then use hash map

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def toCountString(w):
            lst = [0] * 26
            for c in w:
                lst[ord(c) - ord('a')] += 1
            
            res = []
            for i in range(0, 26):
                res.append(str(lst[i]))
                res.append("|")
            
            return "".join(res)
        
        
        d = {}
        for w in strs:
            countStr = toCountString(w)
            if countStr in d:
                d[countStr].append(w)
            else:
                d[countStr] = [w]
        
        return list(d.values())
        
