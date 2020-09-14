class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
        '''
            if a is in d and b is in d:
                rootOfA = find(d, a)
                rootOfB = find(d, b)                
                d[rootOfB] = rootOfA                
            elif a is in d and b is not in d:
                root = find(d, a)
                d[b] = root        
            elif a is not in d and b is in d:
                root = find(d, b)
                d[a] = root                
            elif a is not in d and b is not in d:
                d[b] = a
                d[a] = a
        '''        
        def find(d, cur):
            parent = d[cur]
            while parent != d[parent]:
                d[parent] = find(d, d[parent])
                parent = d[parent]            
            d[cur] = parent
            return parent
        
        # path:
        path = dict()
        for i in range(0, n):
            path[i] = set()            
        for c in connections:
            v1, v2 = c[0], c[1]
            path[v1].add(v2)            
                                                
        redundantConnections = 0
        d = dict()
        for a in range(0, n):
            neighbors = list(path[a])
            for b in neighbors:
                if a in d and b in d:
                    rootOfA = find(d, a)
                    rootOfB = find(d, b)
                    
                    if rootOfA == rootOfB:
                        redundantConnections +=1
                    else:
                        d[rootOfB] = rootOfA                        
                        
                elif a in d and b not in d:
                    root = find(d, a)
                    d[b] = root        
                elif a not in d and b in d:
                    root = find(d, b)
                    d[a] = root                
                elif a not in d and b not in d:
                    d[b] = a
                    d[a] = a
        
        roots = set()
        disconnects = 0
        for i in range(0, n):
            if i in d:
                roots.add(find(d, i))
            else:
                disconnects += 1                
                            
        if disconnects + len(roots) - 1 > redundantConnections:
            return -1
        else:
            return disconnects + len(roots) - 1
        
        return 0
