class LRUCache:

    def __init__(self, capacity: int):
        self.cache = collections.OrderedDict()
        self.size = 0
        self.cap = capacity
                
    def get(self, key: int) -> int:
        
        if key in self.cache:
            val = self.cache[key]            
            self.cache.pop(key)
            self.cache[key] = val            
            return val
            
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        
        if key in self.cache:            
            self.cache.pop(key)
            self.cache[key] = value           
            return            
        else:
            if self.size < self.cap:
                self.cache[key] = value
                self.size += 1                
            else:
                self.cache.popitem(last = False)
                self.cache[key] = value
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
