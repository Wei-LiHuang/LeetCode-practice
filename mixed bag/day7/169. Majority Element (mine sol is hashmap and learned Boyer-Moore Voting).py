class Solution:
    
    # Boyer-Moore Voting Algorithm:
    # store elements count as "potentail"
    # 1, 1, 1, 1, 2, 3, 4 
    # count(1) = 4, since it is bigger then (n / 2), no way any other element can defeat it    
    def majorityElement(self, a: List[int]) -> int:
    
        n, count = len(a), 0        
        curPick = a[0]
        for i in range(1, n):
            
            if a[i] == curPick:
                count += 1
            else:
                count -= 1
                if count < 0:
                    curPick = a[i]
                    count = 0
        
        return curPick
                                                    
    def majorityElement_HashTable(self, a: List[int]) -> int:
        
        n, d = len(a), dict()        
        _max = -float('inf')        
        for i in range(0, n):            
            if a[i] in d:
                d[a[i]] += 1
            else:
                d[a[i]] = 1
                
            _max = max(_max, d[a[i]])
            
            if _max >= (n / 2):
                return a[i]
            
        return 0
