class Solution:
    
    def knightDialer(self, N: int) -> int:
        
        def dfs(keyboard, r, c, memo, nextMemo):
            
            #print(keyboard[r][c])
            
            directions = [[-1, -2], [-2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2]]            
            res = 0
            #nextStep = []
            for d in directions:                
                nr, nc = r + d[0], c + d[1]                
                if nr >= 0 and nr < 4 and nc >= 0 and nc < 3 and keyboard[nr][nc] is not None:
                    #nextStep.append(keyboard[nr][nc])
                    res += memo[keyboard[nr][nc]]
                    
            #print(nextStep)
            nextMemo[keyboard[r][c]] = res % (10**9 + 7)
            return 
        
        
        keyboard = []
        keyboard.append([1, 2, 3])
        keyboard.append([4, 5, 6])
        keyboard.append([7, 8, 9])
        keyboard.append([None, 0, None])
        
        memo = dict()
        for i in range(0, 10):
            memo[i] = 1
                
        for count in range(0, N - 1):            
            nextMemo = dict()
                        
            for i in range(0, 4):
                for j in range(0, 3):
                    if keyboard[i][j] is not None:
                        dfs(keyboard, i, j, memo, nextMemo)                        
            memo = nextMemo
            
        res = 0
        for value in memo.values():
            res += value
            
        return res % (10**9 + 7)
            
