class Solution:
    def longestSubarray(self, a: List[int], k: int) -> int:
        
        '''
            from dicuss:
                [8,2,4,7], l = 0, r = 0, maxIndex = 0, minIndex = 0

                l = 0, r = 0
                    a[r + 1] = 2, a[r + 1] < a[min]
                        -> need check max - a[r + 1] -> False                    
                    res = max(res, r - l + 1) = 1                
                    update maxIndex, minIndex:
                        how to update? use data structure to store next minIndex, maxIndex
                        not heap, because when we need to remove a max from a min heap, it takes linear time to find it
                        use balance BST -> logN time finding/removing a element in tree
                        two deque?
                            one for max, one for min
                            l = 0, r = 0
                            maxQ = [8], minQ = [8]

                            l = 0, r = 1
                            maxQ = [8], minQ = [2], 8 - 2 > 4, move l, maxQ.peek() = a[l], maxQ pop
                            maxQ = [], minQ = [2], l = 1, r = 1

                            l = 1, r = 2
                            maxQ = [4], minQ = [2], 4 - 2 < 4, update ans, res = 2

                            l = 1, r = 3
                            maxQ = [7], minQ = [2], 7 - 2 > 4, move l, minQ.peek() == 2, minQ pop

                            l = 2, r = 3
                            maxQ = [7], minQ = [4], 7 - 4 < 4, update ans, res = 2

                            return res = 2                                                                                    
        '''                        
        
        res = -float('inf')
        n = len(a)
        maxQ, minQ = collections.deque(), collections.deque()
        
        l = 0
        for r in range(0, n):
            
            while len(maxQ) > 0 and a[maxQ[-1]] < a[r]:
                maxQ.pop()
            while len(minQ) > 0 and a[minQ[-1]] > a[r]:
                minQ.pop()
                
            maxQ.append(r)
            minQ.append(r)
            
            _max, _min = a[maxQ[0]], a[minQ[0]]
            
            if _max - _min <= k:
                res = max(res, r - l + 1)
            else:
                if maxQ[0] == l:
                    maxQ.popleft()
                if minQ[0] == l:
                    minQ.popleft()
                    
                l += 1
        
        return res
                
