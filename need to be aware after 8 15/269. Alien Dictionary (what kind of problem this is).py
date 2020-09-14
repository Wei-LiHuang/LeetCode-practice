class Solution:
    
    def alienOrder(self, a: List[str]) -> str:
        
        def dfs(d, cur, path, visited, hasCircle):
            
            if cur in hasCircle:
                return hasCircle[cur]
            
            if cur in visited:
                hasCircle[cur] = True
                return True
            
            visited.add(cur)
            
            neighbors = list(d[cur])
            
            for neighbor in neighbors:
                
                if dfs(d, neighbor, path, visited, hasCircle):
                    hasCircle[cur] = True
                    return True
                                    
            path.append(cur)
            
            hasCircle[cur] = False
                            
            return False
                
        def compareWord(w1, w2):
            
            if w1 == w2:
                return True
            
            # 1. find the first diff:
            diffIndex = -1
            i1, i2 = 0, 0
            while i1 < len(w1) and i2 < len(w2):
                if w1[i1] != w2[i2]:
                    diffIndex = i1
                    break
                else:
                    i1 += 1
                    i2 += 1
            
            if diffIndex == -1:
                if i2 == len(w2):
                    # case "abc" "ab" -> no valid topological sort
                    return False
                elif i1 == len(w1):
                    # case "ab" "abc" -> nothing to compare 
                    return True
            else:
                c1, c2 = w1[diffIndex], w2[diffIndex]
                d[c1].add(c2)
            
            return True
                                                                                
        d = dict()              
        for i in range(0, len(a)):
            for j in range(0, len(a[i])):
                if a[i][j] not in d:
                    d[a[i][j]] = set()
        
        # 1. compare each near by words:
        for i in range(0, len(a) - 1):
            if compareWord(a[i], a[i + 1]) == False:
                return ""
            
        #print(d)
        
        # 2. detect circle:
        hasCircle = dict()
        visited = set()
        path = []
        for key in d.keys():
            if dfs(d, key, path, visited, hasCircle):
                return ""    
            
        path.reverse()                        
        res = ''.join(path)

        return res
                        
    def alienOrder1(self, a: List[str]) -> str:
        
        '''
            if the order is valid, return the order
            else, return ""
                    -> how to check is valid? if it has circle -> its not valid
                    -> how to detect circle? use dfs
                    
                        start from 'w' -> how to get the next step?
            
            
            w r t
            w r f
            e r
            e t t 
            r f t
            
            ues col:
            
                d[w] > [r, t]
                d[r] > [t]
                d[t] > []

                d[w] > [r, t, f]
                d[r] > [t, f]
                d[f] > []

                d[e] > [r]

                d[e] > [r, t]
                d[t] > []

                d[r > [f, t]
                d[f] > [t]
                d[t] > []
                
            use rows:
                wrt
                wrf 
                    -> t > f

                er
                ett
                    -> r > t                                                                                                                             
        '''        
        
        def dfs(d, cur, path, visited, hasCircle):
            
            if cur in hasCircle:
                return hasCircle[cur]
            
            if cur in visited:
                hasCircle[cur] = True
                return True
            
            visited.add(cur)
            
            neighbors = list(d[cur])
            
            for neighbor in neighbors:
                
                if dfs(d, neighbor, path, visited, hasCircle):
                    hasCircle[cur] = True
                    return True
                                    
            path.append(cur)
            
            hasCircle[cur] = False
                            
            return False
                                                                            
        def parseWord(word, d):
            
            n = len(word)
            arr = []
            for i in range(n - 1, -1, -1):
                
                if i < n - 1 and word[i] == word[i + 1]:
                    continue
                
                if word[i] not in d:
                    d[word[i]] = set()                                                        
                d[word[i]].update(arr)
                arr.append(word[i])
                
            return
        
        def parseCol(a, d, r1, r2, c):
                        
            sameR0 = r1
            sameR1 = -1
                                    
            colWord = []
            for r in range(r1, r2 + 1):                
                w = a[r]            
                
                if c >= len(w):
                    colWord.append(None)
                    continue
                
                elif len(colWord) == 0:
                    colWord.append(w[c])
                    
                elif w[c] != colWord[-1]:                    
                    if sameR1 > sameR0:
                        parseCol(a, d, sameR0, sameR1, c + 1)
                        
                        sameR0 = r
                        sameR1 = -1
                    
                    colWord.append(w[c])
                
                elif w[c] == colWord[-1]:
                    sameR1 = r
                                
            if sameR1 > sameR0:
                parseCol(a, d, sameR0, sameR1, c + 1)
                
            parseWord(colWord, d)
                                
            return
                                                       
        d = dict()        
        for i in range(0, len(a)):
            for j in range(0, len(a[i])):
                if a[i][j] not in d:
                    d[a[i][j]] = set()
        
        parseCol(a, d, 0, len(a) - 1, 0)                                
        print(d)
                
        # start form a[0][0]: it must be the smallest -> wrong, if all the words in a start with the same char, it will be wrong -> no ordering
        hasCircle = dict()
        visited = set()
        path = []
        for key in d.keys():
            
            if key == None:
                continue
            
            if None in d[key]:
                return ""
            
            if dfs(d, key, path, visited, hasCircle):
                return ""
                   
        path.reverse()                        
        res = ''.join(path)

        return res
                
            
