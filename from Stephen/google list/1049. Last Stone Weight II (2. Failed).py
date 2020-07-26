class Solution:
    
    def lastStoneWeightII(self, a: List[int]) -> int:
        
        '''
            [2,7,4,1,8,1] -> divide to two groups, 
            find the min(pos group - neg group), where abs(pos group) >= abs(neg group)
            if totalSum = sum(a), posSum = p, negSum = totalSum - p
                -> min(p - totalSum - p) = min(2p - totalSum), where 2p >= totalSum                
                -> p >= totalSum / 2
                
                which also mean finding the max(total - negSum - negSum), where totalSum >= 2 * negSum
                -> negSum <= totalSum / 2
                
                so start from 0, see how far we can reach until (totalSum / 2)
        '''                             
        totalSum = sum(a)
        maxNeg = totalSum // 2   
        n = len(a)        
        
        dp = set()       
        dp.add(0)        
        '''
           對在Set裡的元素都加上a[i],並放入set中 
           -> set中的元素為: 以 a[0], a[1], ..., a[i]為結尾的所有可能 + 都沒有的0
        '''
        curSum = 0
        for i in range(0, n):   
            for val in range(curSum,-1, -1):
            #for val in range(0, curSum + 1): wrong, 會重複算到
                if val in dp:
                    dp.add(val + a[i])
            curSum += a[i]
            #print(dp)
                                                                                
        for i in range(maxNeg, -1, -1):
            if i in dp:
                return (totalSum - 2 * i)
                        
        return 0
