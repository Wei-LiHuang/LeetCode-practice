class Solution:
    
    def hasPath(self, a: List[List[int]], s: List[int], e: List[int]) -> bool:
        
        def findNextStops(a, cur, visited):
            if cur in visited:
                return []
            m, n = len(a), len(a[0])
            r, c, res = cur // n, cur % n, []
            
            visited.add(cur)
                        
            # up
            if r > 0:
                up = r
                while up > 0 and a[up - 1][c] == 0:
                    up -= 1
                if (up * n + c) not in visited:
                    res.append(up * n + c)    
                
            # down
            if r < m - 1:
                down = r
                while down < m - 1 and a[down + 1][c] == 0:
                    down += 1
                if (down * n + c) not in visited:
                    res.append(down * n + c)                
            
            #left
            if c > 0:
                left = c
                while left > 0 and a[r][left - 1] == 0:
                    left -= 1
                if (r * n + left) not in visited:
                    res.append(r * n + left)                
                
            #right
            if c < n - 1:
                right = c
                while right < n - 1 and a[r][right + 1] == 0:
                    right += 1
                if (r * n + right) not in visited:
                    res.append(r * n + right)           
                    
            return res
            
                            
        # edge case:
        m = len(a)
        if m == 0:
            return False
        n = len(a[0])
        if n == 0:
            return False
                
        visited, options = set(), [s[0] * n + s[1]]
        
        while len(options) != 0:            
            curSize, nextOptions = len(options), []
            for i in range(0, curSize):
                cur = options.pop()
                r = cur // n
                c = cur % n
                if r == e[0] and c == e[1]:
                    return True                
                nextOptions.extend(findNextStops(a, cur, visited))
                
            options = nextOptions
            
        
        return False
                
