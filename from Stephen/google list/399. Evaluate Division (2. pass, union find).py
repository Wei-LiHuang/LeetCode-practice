class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        '''
            if a is a forest and b is a forest:                
                a = b * k                
                rootOfB = find(d, b)  -> rootOfB[0] = b * (1/rootOfB[1])  
                rootOfA = find(d, a)  -> rootOfA[0] 
                        = a * (1/rootOfA[1]) 
                        = b * k * (1/rootOfA[1]) 
                        = rootOfB[0] * (rootOfB[1]) * k * (1/rootOfA[1])                                                                                               
                
                d[rootOfA] = [rootOfB, (rootOfB[1]) * k * (1/rootOfA[1])]
                                
            if a is a forest and b is not a forest:      
                a = b * k         
                d[b] = [rootOfA, 1/k * (rootOfA[1])]
                
            if a is not a forest and b is a forest:
                a = b * k
                rootOfB[0] = find(d, b) = b * (1/rootOfB[1])
                b = a * 1/k -> rootOfB = a * 1/k * (1/rootOfB[1])
                d[a] = [rootOfB[0], k * rootOfB[1]]
                                
            if a is not a forest and b is not a forest:                
                
                a = 2.0 * b                
                d[a] = [b, 2,0]
                d[b] = [b, 1.0]        
        '''
        
        def find(d, cur):
            #d[b] = [c, 3.0] -> b = c * 3
            #d[a] = [b, 2.0] -> a = b * 2 -> c * 6                        
            parent = d[cur][0]
            k = d[cur][1]
            while d[parent][0] != parent:                
                node = find(d, parent)
                parent = node[0]
                k *= node[1]
            d[cur] = [parent, k]
            return d[cur]
        
        #set d:
        d = dict()
        n = len(equations)        
        for i in range(0, n):
            a, b = equations[i][0], equations[i][1]
            k = values[i]
            
            if a in d and b in d:
                nodeOfB = find(d, b)
                nodeOfA = find(d, a)
                d[nodeOfA[0]] = [nodeOfB[0], (nodeOfB[1]) * k * (1/nodeOfA[1])]
            elif a in d and b not in d:
                nodeOfA = find(d, a)
                d[b] = [nodeOfA[0], 1/k * (nodeOfA[1])]
            elif a not in d and b in d:
                nodeOfB = find(d, b)
                d[a] = [nodeOfB[0], k * nodeOfB[1]]
            elif a not in d and b not in d:
                d[a] = [b, k]
                d[b] = [b, 1]
        
        #get res:
        res = []
        for q in queries:            
            if q[0] not in d or q[1] not in d:
                res.append(-1.0)
            elif q[0] == q[1]:
                res.append(1.0)
            else:
                node1, node2 = find(d, q[0]), find(d, q[1])
                if node1[0] != node2[0]:
                    res.append(-1)
                else:
                    # q[0] = n1[0] * n1[1]
                    # q[1] = n1[0] * n2[1]
                    # q[0]/q[1] = n1[1] / n2[1]
                    res.append(node1[1]/node2[1])                    
        return res
