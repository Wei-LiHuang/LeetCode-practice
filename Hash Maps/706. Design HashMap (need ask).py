# So the problem is what is the expected time complexity
# To reach O(1), must have a good hash function and probably the range of the input.
# So it says 
#   1.All keys and values will be in the range of [0, 1000000]
#   2.The number of operations will be in the range of [1, 10000]
# Then is easy, use a size = 10000 - list of boolean to store key status: True: pair exist in table, False: pair not exist in table
# And use another size = 10000 - list of int to store value of pair.
# And the put, get, remove will all be O(1) with O(2N) => O(N) space.

# above approach TLE: must be smarter -> use one list, -1 if not exist, other val: exist -> getting 5% -> could be faster?
# chage: for i in range(0, 1000000):self.lst.append(-1) to self.lst = [-1] * 1000000 -> 31% -> could be faster? not this approach maybe?

class MyHashMap(object):

    def __init__(self):
        self.lst = [-1] * 1000000
        #for i in range(0, 1000000):
            #self.lst.append(-1)


    def put(self, key, value):                    
        self.lst[key - 1] = value
        

    def get(self, key):     
        return self.lst[key - 1]
        

    def remove(self, key):
        self.lst[key - 1] = -1
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
