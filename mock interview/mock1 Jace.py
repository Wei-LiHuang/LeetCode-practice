"""
Implement a data structure that is initialized with an integer K.

This data structure should have two methods:
1) A method that allows the caller to insert an integer, one at a time.
2) A method that will return the product of the last K inserted integers.

K = 3

2 3 4 5

getProduct() -> 60
"""
import collections

class Solution:
    
    def __init__(self):
        self.k = k
        self.q = collections.deque()
        self.curProduct = 1
        self.zeroInQueue = 0
        
    def insert(self, val):
        
        if len(self.q) == self.k:
            popped = self.q.popleft()
            if popped == 0:
                self.zeroInQueue -= 1
            else:
                self.curProduct = self.curProduct // popped
        
        if val == 0:
            self.zeroInQueue += 1
            
        self.q.append(val)
        if val != 0:
            self.curProduct *= val
        
    def getProduct(self, k):
        if len(self.q) == 0:
            return 0
        elif self.zeroInQueue > 0:
            return 0
        else:            
            return self.curProduct
        
'''        
2 3 4 5 6
2 0 4 5 6

p0 = 2
p1 = 2 * 3
p2 = 2 * 3 * 4
...
p5 = 2 * 3 * 4 * 5 * 6

k = 3 -> 4 * 5 * 6

p5 / p1

n elements
k elements to make product

e[n - 1] * e[n - 2] * ... * e[n - k]

pi = e[0] * e[1] * ... * e[i]


=====
2 3 0 4

p0 = 2
p1 = 2 * 3
p2 = 2 * 3
p3 = 2 * 3 * 4 = 0


record the last pos of 0 element => 2

e[n - 1] to e[n - k] -> O(N) 




return (p[n - 1] / p[n - k - 1])



'''
getProduct(2) -> 30
getProduct(3) -> 120
getProduct(4) -> 360
        
obj = Solution(3)

obj.insert(0)
obj.insert(0)
obj.insert(0)
obj.insert(3)
obj.insert(10)
print(obj.getProduct())
obj.insert(4)
obj.insert(5)
print(obj.getProduct())
