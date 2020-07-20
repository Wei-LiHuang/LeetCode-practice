class RandomizedSet:
    
    '''
        How do you modify your code to allow duplicated number?                                      
    '''

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = dict() # d[val] = [count, [i1, i2, ..., i n]]
        self.curSize = 0
        self.arr = []


    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        
        #self.curSize += 1        
        if val in self.d:
            #self.d[val][0] += 1
            #self.d[val][1].append(self.curSize - 1)
            return False
        else:
            self.curSize += 1       
            self.arr.append(val)
            self.d[val] = [1, [self.curSize - 1]]        
        
        return True
                                    
    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.d:
            return False
        
        #print(self.d)
        
        lastIndexInArr = self.d[val][1][-1]
        lastElementInArr = self.arr[-1]
        self.d[lastElementInArr][1][-1] = lastIndexInArr
        
        self.arr[-1], self.arr[lastIndexInArr] = self.arr[lastIndexInArr], self.arr[-1]        
        self.arr.pop()
        self.curSize -= 1
        
        self.d[val][1].pop()
        self.d[val][0] -= 1
        if self.d[val][0] == 0:
            del self.d[val]
            
        return True                                        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return choice(self.arr)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
