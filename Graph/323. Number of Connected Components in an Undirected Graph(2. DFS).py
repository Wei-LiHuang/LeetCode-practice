class Solution:
    
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        def dfs(cur, edges, status):
            
            if status[cur] == True:
                return 
            
            status[cur] = True
            if cur in edges:
                nextSteps = edges[cur]
                for i in nextSteps:
                    dfs(i, edges, status)
            
            return
                                                                            
        e = dict()
        for pair in edges:
            if pair[0] in e:
                e[pair[0]].append(pair[1])
            else:
                e[pair[0]] = [pair[1]]
            
            if pair[1] in e:
                e[pair[1]].append(pair[0])
            else:
                e[pair[1]] = [pair[0]]
        
        status = [False] * n
        
        res = 0
        for i in range(0, n):            
            if status[i] == False:
                res += 1
                dfs(i, e, status)
                
        return res
        
        
