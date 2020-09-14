class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        
        '''
            1. brute force:
                list out all the subarray, return the max one
                -> time: O(N^2)
                
            2. sliding window:
                move right when (tiring day num) > (non tiring day num) or (tiring day num) == (non tiring day num) and next day is a tiring day
                move left when (tiring day num) == (non tiring day num) and next day is not a tiring day
                -> time: O(N), but seems a little bit complicated
            
            3. dp:
                tiring[i]: tiring day count from a[0] to a[i]
                nTiring[i]: non tiring day count from a[0] to a[i]
                
                from hint:
                    first create a new array a[]:
                        if the day i is a tiring day -> set a[i] = 1
                        else: set a[i] = -1                        
                    so the goal now is to find a max len subarray with positive sum                    
                    -> pre sum:
                        tgt: > 0
                        define preSum[i]: the sum from a[0] to a[i]
                        
                        -> so if a[i] to a[j] is a "Well-Performing Interval"
                        -> a[i] + a[i + 1] + ... + a[j - 1] + a[j] > 0
                        -> preSum[j] - preSum[i - 1] > 0
                        -> we can now get if preSum[j] > preSum[i - 1], then a[i] ~ a[j] is a solution
                        
                        every preSum is stored in a container, do we need to scan it every time we get a new preSum[i]?
                        no, we should maintain some kind of order:
                        
                        
                        hours = [9,9,6,0,6,6,9], a = [1, 1, -1, -1, -1, -1, 1]                        
                        init: 
                            preSum: [[preSum: 0, index: -1]]                            
                        add a[0] = 1:
                            _sum = 0 + 1
                            _sum > preSum[0] -> maxL = max(0, i - preSum[0][1]) = 1
                            preSum: [[preSum: 0, index: -1], [preSum: 1, index: 0]]
                        
                        add a[1] = 1:
                            _sum = 1 + 1
                            _sum > preSum[0] -> maxL = max(0, i - preSum[0][1]) = 2
                            _sum > preSum[1] -> maxL = max(0, i - preSum[1][1]) = max(1, 2) = 2
                            preSum: [[preSum: 0, index: -1], [preSum: 1, index: 0], [preSum: 2, index: 1]]
                            
                        add a[2] = -1:
                            _sum = 2 + -1 = 1
                            _sum > preSum[0] -> maxL = max(0, i - preSum[0][1]) = 3                            
                            preSum: [[preSum: 0, index: -1], [preSum: 1, index: 0], [preSum: 2, index: 1], [preSum: 1, index: 3]]
                          
                        add a[3] = -1:
                            _sum = 1 + -1 = 0
                            no smaller element in preSum, maxL still = 2            
                            preSum: [[preSum: 0, index: -1], [preSum: 1, index: 0], [preSum: 2, index: 1], [preSum: 1, index: 3],  [preSum: 0, index: 4]]
                        
                            
                        -> preSum should only store elements with: [decreasing preSum val, smaller index]                                                        
        '''
        
        a = []
        for val in hours:
            if val > 8:
                a.append(1)
            else:
                a.append(-1)
                
        preSum = [[0, -1]]
        _sum, maxL = 0, 0
        
        for i in range(0, len(a)):
            _sum += a[i]
            
            if _sum < preSum[-1][0]:
                preSum.append([_sum, i])
                continue
                
            else:
                for j in range(0, len(preSum)):
                    if _sum > preSum[j][0]:
                        maxL = max(maxL, i - preSum[j][1])
                        break
                                                            
        return maxL
            
