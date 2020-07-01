class Solution:
    
    def permuteUnique(self, a):
        
        def dfs(path, d):
            
            if len(path)==len(a):
                ans.append(path[:])
                
            for x in d.keys():  # dont pick duplicates                                                                                
                if d[x] > 0:
                    path.append(x)
                    d[x] -= 1
                    dfs(path, d)
                    path.pop()
                    d[x] += 1
                            
        d = dict()
        for i in a:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        
        ans = []
        dfs([], d)
        return ans
