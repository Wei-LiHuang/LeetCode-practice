# Undirected graph -> can't use dfs hasCircle
# add one edge at one time, check does it make any circle
# subGrapgh1, subGraph2 -> merge

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n, vToSet, setToV = len(edges), dict(), dict()
        
        newSet = 0
        for e in edges:            
            if e[0] not in vToSet and e[1] not in vToSet:                
                vToSet[e[0]] = newSet
                vToSet[e[1]] = newSet                
                setToV[newSet] = [e[0], e[1]]
                newSet += 1
                
            elif e[0] not in vToSet and e[1] in vToSet:                
                vToSet[e[0]] = vToSet[e[1]]
                setToV[vToSet[e[1]]].append(e[0])
                
            elif e[0] in vToSet and e[1] not in vToSet:
                vToSet[e[1]] = vToSet[e[0]]
                setToV[vToSet[e[0]]].append(e[1])
                
            elif e[0] in vToSet and e[1] in vToSet:                
                
                if vToSet[e[0]] == vToSet[e[1]]:
                    return e
                
                elif vToSet[e[0]] != vToSet[e[1]]:
                    
                    set0 = vToSet[e[0]]                    
                    set1 = vToSet[e[1]]                    
                    
                    allInSetE0 = setToV[set0]
                    
                    for v in allInSetE0:
                        vToSet[v] = set1                     
                    
                    setToV[set1].extend(allInSetE0)                                        
                    del setToV[set0]
                    
                    
        return []
            
