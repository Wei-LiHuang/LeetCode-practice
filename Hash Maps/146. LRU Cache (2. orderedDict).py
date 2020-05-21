#ordered_dict approach

class LRUCache:
    
    def __init__(self, capacity: int):
        self.dic = collections.OrderedDict()
        self.cap = capacity
        self.cur = 0

    def get(self, key: int) -> int:
        if key in self.dic:
            val = self.dic.pop(key)
            self.dic[key] = val
            return val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        
        if key in self.dic:
            self.dic.pop(key)
            self.dic[key] = value
            return
        
        else:            
            if self.cap > self.cur:                
                self.dic[key] = value
                self.cur += 1
                return
            
            elif self.cap == self.cur:
                drop = self.dic.popitem(last=False)
                self.dic[key] = value
                return
                
                
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
