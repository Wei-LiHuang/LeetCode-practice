# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
                
        '''
            create a arr for all nodes
            calculate all preSum:
                if sum(a[i]...a[j]) == 0 -> sum(a[0]...a[j]) - sum(a[0]...a[i - 1]) == 0
                    -> sum(a[0]...a[j]) == sum(a[0]...a[i - 1])            
                       so we put preSum sum(a[0]...a[i - 1]) in hash table
                       
            once we found sum(a[0]...a[j]) == sum(a[0]...a[i - 1]) -> a[i] ~ a[j] should be removed
            the preSum end at a[i] ... a[j] should also be removed from the hash table
            
            ----AND THE SUM COUNTER SHOULD BE SET TO "preSum(a[0]...a[i - 1])" <- where I failed-----
        
        '''
        
        a = []
        shift = head
        while shift is not None:
            temp = shift.next
            shift.next = None
            a.append(shift)                                 
            shift = temp

        n = len(a)             
        preSum = [0] * n      
        
        d = dict()             
        d[0] = -1
        
        _sum = 0
        needRemove = set()
        for i in range(0, n):            
            _sum += a[i].val   
            
            if _sum in d:
                leftIndex = d[_sum]                                               
                for j in range(leftIndex + 1, i):
                    if j not in needRemove:
                        del d[preSum[j]]
                        needRemove.add(j)                    
                needRemove.add(i)
                _sum = preSum[leftIndex]
            else:                        
                d[_sum] = i                
                preSum[i] = _sum
            
            
        nodeLeft = []
        for i in range(0, n):
            if i not in needRemove:
                nodeLeft.append(a[i])
                if len(nodeLeft) > 1:
                    nodeLeft[-2].next = nodeLeft[-1]
        
        if len(nodeLeft) == 0:
            return None
                                                                                    
        return nodeLeft[0]

            
                
