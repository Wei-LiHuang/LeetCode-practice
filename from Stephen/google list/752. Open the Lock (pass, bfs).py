class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        '''
            shortest path -> BFS                                    
        '''     
        
        def toString(cur):
            _str = ""
            for v in cur:
                _str += str(v)
            return _str
                    
        def checkDeadEnds(deadendsSet, _str):            
            if _str in deadendsSet:
                return False
            
            return True
        
        def findNextStep(deadendsSet, curLock, visited):
            
            directions = [[1,0,0,0], [-1,0,0,0],
                          [0,1,0,0], [0,-1,0,0],
                          [0,0,1,0], [0,0,-1,0],
                          [0,0,0,1], [0,0,0,-1]]            
            nextSteps = []            
            for d in directions:
                cur = [curLock[0] + d[0], curLock[1] + d[1], curLock[2] + d[2], curLock[3] + d[3]]
                for i in range(0, 4):
                    if cur[i] == -1:
                        cur[i] = 9
                    elif cur[i] == 10:
                        cur[i] = 0
                        
                _str = toString(cur)                        
                if checkDeadEnds(deadendsSet, _str) and _str not in visited:
                    nextSteps.append(cur)
                    visited.add(_str)
                    
            return nextSteps
                                                                                                            
        deadendsSet = set()
        for d in deadends:
            deadendsSet.add(d)
                    
        lock = [0,0,0,0]
        
        if toString(lock) in deadendsSet:
            return -1
        
        q = collections.deque()
        q.append(lock)
                
        moves = 0
        visited = set()
        while len(q) > 0:
            curSize = len(q)
            for i in range(0, curSize):
                cur = q.pop()
                if toString(cur) == target:
                    return moves               
                nextSteps = findNextStep(deadendsSet, cur, visited)
                q.extendleft(nextSteps)
            moves += 1
            
        return -1
            
