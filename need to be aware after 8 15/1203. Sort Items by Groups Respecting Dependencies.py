class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        
        # 1. create graph: beforeItems[i] = j -> (j -> i) -> reverse (i -> j) -> edge[i] = [j]
        edge = dict()
        for i in range(0, n):            
            if i not in edge:
                edge[i] = list()
            edge[i].extend(beforeItems[i])

        # 2. topological sort all items:
        def detect(cur, edge, visited, hasCircle, path):
            
            if cur in hasCircle:
                return hasCircle[cur]
            
            if cur in visited:
                hasCircle[cur] = True
                return True
            
            visited.add(cur)
            
            if cur in edge:
                for neighbor in edge[cur]:
                    if detect(neighbor, edge, visited, hasCircle,path):
                        hasCircle[cur] = True
                        return True
            
            path.append(cur)
            hasCircle[cur] = False
            return False                            
        
        visited, hasCircle, path = set(), dict(), []        
        for i in range(0, n):
            if detect(i, edge, visited, hasCircle, path):
                return []
                     
        # 3. sort group and create beforeGroups:
        groupToItems = dict()
        for i in range(0, n):
            g = group[i]
            if g not in groupToItems:
                groupToItems[g] = list()                
            groupToItems[g].append(i)            
        #print(groupToItems)
        
        beforeGroups = dict()
        for gid in groupToItems.keys():
            items = groupToItems[gid]         
            
            if gid not in beforeGroups:
                beforeGroups[gid] = set()
            
            for item in items:
                beforeItemList = beforeItems[item]
                for bid in beforeItemList:
                    if group[bid] != gid:
                        beforeGroups[gid].add(group[bid])
        
        visited, hasCircle, groupPath = set(), dict(), [] 
        #print(beforeGroups)
        for gid in beforeGroups.keys():
            if detect(gid, beforeGroups, visited, hasCircle, groupPath):
                return []        
        #print(groupPath)
                
        # 4. merge groups:
        inGroupOrder = dict()
        for i in range(0, len(path)):
            inGroupOrder[path[i]] = i
        
        def cmp(i1, i2):
            return inGroupOrder[i1] - inGroupOrder[i2]
                    
        res = []
        for gid in groupPath:
            groupItemList = groupToItems[gid]
            groupItemList.sort(key = cmp_to_key(cmp))            
            res.extend(groupItemList)                                
        
        return res
