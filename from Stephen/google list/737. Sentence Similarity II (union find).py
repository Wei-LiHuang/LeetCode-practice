class Solution:
    
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        
        '''
            1. [w1, w2] in pairs:
                a. w1 is a forest, w2 is a forest:
                    -> point a's root to b's root
                    -> update from a by find(d, a)
                
                b. w1 is a forest, w2 is not a forest:
                    -> point b to a's root
                    
                c. w1 is a not forest, w2 is a forest:
                    -> point a to b's root
                    
                d. w1 is not a forest, w2 is not a forest:
                    -> make a become b's root
                    
            2. scan w in words:
                if any words not in d:
                    it is one node forest -> d[w] = w, find(d, w) = w
        '''
        
        def find(d, w):
            parent = d[w]
            while d[parent] != parent:
                parent = find(d, parent)
            
            d[w] = parent
            return parent
        
        d = dict()
        
        for p in pairs:
            w1, w2 = p[0], p[1]
            
            if w1 in d and w2 in d:
                rootOfW1 = find(d, w1)
                rootOfW2 = find(d, w2)                
                d[rootOfW2] = rootOfW1
                continue
                
            elif w1 in d and w2 not in d:
                rootOfW1 = find(d, w1)
                d[w2] = rootOfW1
                continue
                
            elif w1 not in d and w2 in d:
                rootOfW2 = find(d, w2)
                d[w1] = rootOfW2
                continue
                
            elif w1 not in d and w2 not in d:
                d[w2] = w1
                d[w1] = w1
                continue
                
        if len(words1) != len(words2):
            return False
        
        for i in range(0, len(words1)):
            w1, w2 = words1[i], words2[i]
            
            if w1 not in d and w2 not in d:
                if w1 != w2:
                    return False
            elif w1 in d and w2 not in d:
                return False
            
            elif w1 not in d and w2 in d:
                return False
            
            elif w1 in d and w2 in d:
                if find(d, w1) != find(d, w2):
                    return False
                                                
        return True
        
