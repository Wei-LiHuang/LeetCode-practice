#satrt from small side, try big side next time

class Solution(object):

    def merge(self, n1, m, n2, n):
        
        if n == 0:
            return
        
        i1, i2 = 0, 0
        
        while i1 < m:            
            v1 = n1[i1]
            v2 = n2[i2]
            
            if v1 > v2:
                
                #v2 to v1:
                temp = v1
                n1[i1] = v2
                i1 += 1
                
                #v1 to n2:
                n2[i2] = temp # need check: is n2[i2] the smallest?                
                for i in range(i2, n - 1):
                    if n2[i] > n2[i + 1]:
                        n2[i], n2[i + 1] = n2[i + 1], n2[i]
                    else:
                        break                       
            elif v1 == v2:
                i1 += 1
                                
            else: # v1 < v2
                i1 += 1
                
        # now i1 = m, and all n2 > n1:
        for j in range(i2, n):
            n1[m + j] = n2[j]
            
            
        
        
