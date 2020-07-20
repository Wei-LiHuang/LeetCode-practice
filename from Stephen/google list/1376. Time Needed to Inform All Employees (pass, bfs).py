class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        '''
            employee: 0 ~ n - 1
            headID = k
            manager[i]: employee i's manager id
            informTime[i]: employee i infor his sub time                                
            -> BFS
        '''
                                    
        d = dict()
        for i in range(0, n):
            if i != headID:
                managerOfI = manager[i]
                if managerOfI in d:
                    d[managerOfI].append(i)
                else:
                    d[managerOfI] = [i]
                    
        q = collections.deque()
        q.append(headID)
        
        timePass = dict()
        timePass[headID] = 0
        
        res = 0
        while len(q) > 0:
            curSize = len(q)
            for i in range(0, curSize):
                cur = q.pop()
                if cur in d:
                    subs = d[cur]
                    for sub in subs:
                        timePass[sub] = timePass[cur] + informTime[cur]
                        res = max(res, timePass[sub])
                    q.extendleft(subs)
                
        return res
                
            
