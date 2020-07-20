class Solution:
    
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        if n == 1:
            return [0]
            
        
        d, leaves = dict(), set()
        for e in edges:
            v1, v2 = e[0], e[1]
            if v1 in d:
                d[v1].add(v2)
                if v1 in leaves:
                    leaves.remove(v1)
            else:
                d[v1] = set()
                d[v1].add(v2)
                leaves.add(v1)
            
            if v2 in d:
                d[v2].add(v1)
                if v2 in leaves:                    
                    leaves.remove(v2)
            else:
                d[v2] = set()
                d[v2].add(v1)
                leaves.add(v2)
        
        #print(leaves)
        nodeLeft = n
        q = collections.deque(leaves)
        while len(q) > 0:
            
            curSize = len(q)            
            nodeLeft -= curSize
            if nodeLeft == 0:
                if curSize == 1:
                    return [q[0]]
                elif curSize == 2:
                    return [q[0], q[1]]                
                                             
            for i in range(0, curSize):
                leaves = q.pop()                
                parent = d[leaves].pop()
                del d[leaves]
                d[parent].remove(leaves)
                if len(d[parent]) == 1:
                    q.appendleft(parent)
            
        return[]
