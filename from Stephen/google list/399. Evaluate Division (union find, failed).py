class Solution:
    
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        '''
            find(d, curNode): find the ratio between curNode and the root node
                -> curNode / parent = k -> curNode = parent * k

            how? Assume curNode -> ni -> nj -> parentNode
                nj = parentNode * d[nj][1]
                ni = nj * ki = parentNode * d[nj][1] * d[ni][1]
                curNode = ni * d[curNode][1] = parentNode * d[nj][1] * d[ni][1] * d[curNode][1]
            so k = d[nj][1] * d[ni][1] * d[curNode][1]

            and we set d[curNode] = [parentNode, k]
        '''
        def find(d, curNode):            
            parent = d[curNode][0]
            if d[parent][0] == curNode:
                return 1.0            
            
            k = d[curNode][1]
            while parent != d[parent][0]:
                k *= find(d, parent)
                parent = d[parent][0]
                                        
            d[curNode] = [parent, k]
            return k
            
        #build dict:        
        d = dict()
        n = len(equations)
        for i in range(0, n):
            v1, v2, val = equations[i][0], equations[i][1], values[i]
            
            #print([v1, v2])
            '''
                v1, v2 are forest -> v1 has its parent and so does v2. connect v1 to v2's parent

                v1 is forest -> v1 has its parent. connect v2 to v1's parent.

                v2 is forest -> v2 has its parent. connect v1 to v2's parent.

                v1, v2 are not forest -> use v1 as parent, so d[v1] = [v1, 1.0], d[v2] = [v1, 1 / values]
            '''
            #v1, v2 are not forest -> use v1 as parent, so d[v1] = [v1, 1.0], d[v2] = [v1, 1 / values]
            if v1 not in d and v2 not in d:
                d[v1] = [v2, val]
                d[v2] = [v2, 1.0]
            #v2 is forest -> v2 has its parent. connect v1 to v2's parent.
            elif v2 in d and v1 not in d:
                v2Parent = d[v2][0]
                d[v1] = [v2, val]
                find(d, v1)                
            #v1 is forest -> v1 has its parent. connect v2 to v1's parent.
            elif v1 in d and v2 not in d:
                v1Parent = d[v1][0]
                d[v2] = [v1, 1 / val]
                find(d, v2)
            #v1, v2 are forest -> v1 has its parent and so does v2. connect v1 to v2's parent
            elif v1 in d and v2 in d:                
                '''
                    v1 = p1 * kv1
                    v2 = p2 * kv2                
                    v1 = val * v2                
                    (p1 * kv1) = val * (p2 * kv2)
                    p1 = (val * kv2 / kv1) * p2                
                '''                                                
                v1Parent = d[v1][0]
                kV1 = d[v1][1]
                
                v2Parent = d[v2][0]
                kV2 = d[v2][1]
                
                if v1Parent != v2Parent:
                    d[v1Parent][0] = v2Parent
                    d[v1Parent][1] = (val * kV2 / kV1)
                    find(d, v1)    
                                                                                                                                                    
        #querys:
        res = []        
        for q in queries:
            v1, v2 = q[0], q[1]            
            if v1 not in d or v2 not in d:
                res.append(-1.0)
            elif v1 == v2:
                res.append(1.0)
            else:            
                find(d, v1)
                find(d, v2)
                
                if d[v1][0] == d[v2][0]:
                    '''
                        a = ka * parent
                        b = kb * parent                
                        a / b = ka / kb                
                    '''                    
                    res.append(find(d, v1) / find(d, v2))
                else:
                    res.append(-1.0)
                
        return res
