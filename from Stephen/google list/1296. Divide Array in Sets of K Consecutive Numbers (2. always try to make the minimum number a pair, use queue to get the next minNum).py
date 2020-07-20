class Solution:
    
    def isPossibleDivide(self, a: List[int], k: int) -> bool:
        
        '''
        [3,2,1,2,3,4,3,4,5,9,10,11] - > [1, 2, 2, 3, 3, 3, 4, 4, 5, 9, 10, 11]
        always try to make the minimum number a pair                          
        
        Edit 1: no need to sort
        Edit 2: sort, use deque to get the min num
        '''                            
        a.sort()
        d = dict()
        n = len(a)
        totalCount = n        
        q = collections.deque()
        for i in range(0, n):
            if a[i] in d:
                d[a[i]] += 1
            else:
                d[a[i]] = 1            
                q.append(a[i])
                            
        minNum = q[0]
        count = 0
        while count < totalCount:
            d[minNum] -= 1
            if d[minNum] == 0:
                del d[minNum]
            for i in range(1, k):
                if minNum + i not in d:
                    return False
                d[minNum + i] -= 1
                if d[minNum + i] == 0:
                    del d[minNum + i]                    
            count += k
            if count == totalCount:
                break
            
            while q[0] not in d:
                q.popleft()
            minNum = q[0]
            
                                
        return True
        
