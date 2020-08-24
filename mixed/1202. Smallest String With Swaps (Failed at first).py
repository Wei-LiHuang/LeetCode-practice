class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        
        def find(d, cur):
            parent = d[cur]
            while parent != d[parent]:
                d[parent] = find(d, d[parent])
                parent = d[parent]
            d[cur] = parent                
            return d[cur]
                
        d = dict()
        for p in pairs:
            a, b = p[0], p[1]
            if a in d and b in d:
                r1 = find(d, a)
                r2 = find(d, b)
                d[r2] = r1
            elif a in d and b not in d:
                r = find(d, a)
                d[b] = r
            elif a not in d and b in d:
                r = find(d, b)
                d[a] = r
            elif a not in d and b not in d:                
                d[a] = a
                d[b] = a
            
        a = [] 
        roots = dict()
        for i in range(0, len(s)):            
            a.append(s[i])
            if i in d:
                r = find(d, i)
                if r not in roots:
                    roots[r] = []
                    roots[r].append([s[i]])
                    roots[r].append([i])
                else:
                    roots[r][0].append(s[i])
                    roots[r][1].append(i)
            
        for group in roots.values():            
            indexArr = group[1]
            charArr = group[0]
            charArr.sort()            
            for i in range(0, len(indexArr)):
                a[indexArr[i]] = charArr[i]
                                
        ans = ""
        for c in a:
            ans += c
            
        return ans
                
                
