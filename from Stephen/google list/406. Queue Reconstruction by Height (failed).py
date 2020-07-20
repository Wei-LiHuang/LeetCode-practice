class Solution:
    def reconstructQueue(self, a: List[List[int]]) -> List[List[int]]:
        '''
            a[i] = [h, k]: h -> the height of the person, k -> k is the number of taller or equal height people before a[i]
            
            so we have len(a) people, who should we put first?            
                sort a by k then h:                
                [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
             -> [[5,0],[7,0],[6,1],[7,1],[5,2],[4,4]]
             
                or
                sort a by h then k:
                [[4,4],[5,0],[5,2],[6,1],[7,0],[7,1]]                
                [[7,0],[7,1],[6,1],[5,0],[5,2],[4,4]]                                                      
                
                [x,x,x,x,x,x]
                [x,x,x,x,4,x]
                [x,x,5,x,4,x]
                [x,5,5,x,4,x]
                [x,5,5,6,4,x]
                
                
        '''
        
        def cmp(a1, a2):
            if a1[0] == a2[0]:
                return a1[1] - a2[1]
            else:
                return a2[0] - a1[0]
            
        a.sort(key = cmp_to_key(cmp))
        n = len(a)
        #print(a)
        
        # start from the shortest person:
        pos = []
        
        for i in range(0, n):
            pos.insert(a[i][1], a[i])

        return pos
