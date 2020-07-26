class Solution:
    
    def reconstructQueue(self, a: List[List[int]]) -> List[List[int]]:
        '''
            sort the list:
                [[7,0], [4,4], [7,1], [5,0], [6,1],                 
             -> [[7,0], [7,1], [6,1], [5,0], [5,2], [4,4]]                                                                                                    
                
                7
                7,7
                7,6,7
                5,7,6,7
                5,7,5,6,7
                5,7,5,6,4,7
                
                假設 a[0] 到 a[i - 1] 都已排好:
                    a[i] = [x, y]                    
                    已知x為剩下的元素中最大者, 且其前面會站幾個人也已確定(後面都不影響站位計算)                    
                    -> 直接把 a[i] 放在以排序數列之第 y 個位置                                                            
        '''        
        def cmp(v1, v2):
            if v1[0] == v2[0]:
                return v1[1] - v2[1]
            else:
                return v2[0] - v1[0]
            
        a.sort(key = cmp_to_key(cmp))
        #print(a)
        res = []        
        for p in a:            
            res.insert(p[1], p)                            
        return res
