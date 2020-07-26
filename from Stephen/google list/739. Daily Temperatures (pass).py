class Solution:
    
    def dailyTemperatures(self, a: List[int]) -> List[int]:
        
        '''
        [73, 74, 75, 71, 69, 72, 76, 73]
        [73, 74, 75, 71, 69, 72, 76,  0], q: 73
        [73, 74, 75, 71, 69, 72,  0,  0], q: 76, del 73
        [73, 74, 75, 71, 69,  1,  0,  0], q: 72, 76
        [73, 74, 75, 71,  1,  1,  0,  0], q: 69, 72, 76
        [73, 74, 75,  2,  1,  1,  0,  0], q: 71, 72, 76 ...
        
        '''                
        q = collections.deque()
        n = len(a)
        res = [0] * n
        for i in range(n - 1, -1, -1):            
            if i == n - 1:
                q.append(i)
                continue
            else:
                
                while len(q) > 0 and a[q[0]] <= a[i]:
                    q.popleft()
                    
                if len(q) == 0:
                    q.append(i)
                    continue
                else:
                    res[i] = q[0] - i
                    q.appendleft(i)
                    continue
        
        return res
                    
        
