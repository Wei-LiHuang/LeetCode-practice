class Solution:
    def findCircleNum(self, a: List[List[int]]) -> int:        
        '''
            looks like coloring question
            when a a[i][j] is 1, then we use dfs to color all 1 that connect to a[i][j]
            then count the number of different color in a                        
                
        
            but it is a little different in finding neighbors:
            -> it is a union find problem
            
            a[i][j] == 1, means i and j are firends
            
            1. if i is a forest and j is also a forest:
                connect j's root to i's root
            
            2. if i is a forest and j is not a forest:
                connect j to i's root
            
            3. if i is not a forest and j is a forest:
                connect i to j's root
                
            4. if i is not a forest and j is not a forest:
                set i's root to j                    
        '''    
        def find(node, d):            
            parent = d[node]
            while parent != d[parent]:
                parent = find(parent, d)
            d[node] = parent
            return parent
                                                                
        n = len(a)
        if n == 0:
            return 0
        
        # build dict:
        d = dict()
        for i in range(0, n):
            for j in range(0, n):
                if a[i][j] == 1:
                    if i not in d and j not in d:                                        
                        d[i] = j
                    elif i in d and j not in d:
                        rootOfI = find(i, d)
                        d[j] = rootOfI
                    elif i not in d and j in d:
                        rootOfJ = find(j, d)
                        d[i] = rootOfJ
                    elif i in d and j in d:
                        rootOfI = find(i, d)
                        rootOfJ = find(j, d)
                        d[rootOfI] = rootOfJ
        
        #print(d)
        # count root:
        rootSet = set()
        for i in range(0, n):
            for j in range(0, n):
                root = find(i, d)
                if root not in rootSet:
                    rootSet.add(root)
                    
        return len(rootSet)
