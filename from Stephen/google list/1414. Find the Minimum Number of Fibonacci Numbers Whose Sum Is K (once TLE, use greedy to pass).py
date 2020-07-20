class Solution:
    
    def findMinFibonacciNumbers(self, k: int) -> int:
        '''
            tgt = k
            assume we have a seq of fib: [1, 1, 2, 3, 5, 8, 13, ..., endVal], endVal >= k
                (any fib bigger than k will not be in the sloution)
            
            since the fib can be use multiple times, this is more like coin change than pre sum            
                -> how to reach the tgt using the min number of coins
                -> shortest path question -> bfs          
                
            TLE, how can we ddo better?
            fib[i] = fib[i - 1] + fib[i - 2]
            so maybe we dont need to use all the coins? -> use the nearest one -> Greedy                    
        '''
        def fibNumToEndVal(k):
            fib = [1, 1]
            while fib[-1] < k:
                fib.append(fib[-1] + fib[-2])
            return fib
        
        
        # 1. setup a fib sequence:
        coins = fibNumToEndVal(k)        
        #print(coins)
        
        #'''
        # 2. BFS:
        q = collections.deque()
        q.append(k)
        
        visited = set()
        step = 0
        while len(q) > 0:
            curSize = len(q)
            for i in range(0, curSize):
                popped = q.pop()                                
                if popped == 0:
                    return step                
                for i in range(len(coins) - 1, -1, -1):
                    c = coins[i]
                    nextStep = popped - c
                    if nextStep >= 0 and nextStep not in visited:
                        q.appendleft(nextStep)
                        visited.add(nextStep)                        
                        coins = coins[0:i + 1]                    
                        break
            #print(q)
            step += 1
        #'''                
        return 0
