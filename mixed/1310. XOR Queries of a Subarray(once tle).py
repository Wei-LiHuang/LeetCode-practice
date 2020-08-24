class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        
        '''
            use presum?
            
            // Because A ^ A ^ B = B
        '''
        
        a = []
        for i in range(0, len(arr)):
            if i == 0:
                a.append(arr[i])
                continue
            else:
                a.append(arr[i] ^ a[-1])
        
        res = []
        for q in queries:
            i1, i2 = q[0], q[1]            
            if i1 == 0:
                res.append(a[i2])
            else:
                res.append(a[i1 - 1] ^ a[i2])
            
        
        return res
        
        
        
        
    def xorQueries_StraightForward_TLE(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        '''
            xor -> 11, 00 -> 0, 10, 01 -> 1
            
            1. turn all element to bitForm
            2. do the operation
        '''
        def turnToBitForm(val):
            res = [0] * 32
            startIndex = int(math.log2(val))
            for i in range(startIndex, -1, -1):
                
                if val >= 2 ** i:
                    res[i] = 1
                    val -= 2 ** i
                else:
                    res[i] = 0
        
            return res
        
        def doXOR(b1, b2):
            res = [0] * 32
            val = 0
            for i in range(0, 32):
                if b1[i] == b2[i]:
                    res[i] = 0
                else:
                    res[i] = 1                                       
            return res
                 
        def turnToTenBased(b):
            val = 0
            for i in range(0, 32):
                val += (2 ** i) * b[i]
            return val
        
        bitForms = []
        for e in arr:
            bitForms.append(turnToBitForm(e))
                      
        res = []
        for q in queries:
            start, end = q[0], q[1]                                                
            b = bitForms[start]        
            for i in range(start + 1, end + 1):
                b = doXOR(b, bitForms[i])

            res.append(turnToTenBased(b))
            
        
        return res
        
        
