# need ask python private class?

class Node:
    
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        
    def link(self, nextNode):
        #print("next is set to:" + str(nextNode))
        self.next = nextNode
                        
class MyHashMap:
    
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lst = []
        for i in range(0, 10000):
            dummy = Node(-1, -1)
            self.lst.append(dummy)
                
    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.                        
        """
        hashVal = key % len(self.lst)
        
        newNode = Node(key, value)

        pre = self.lst[hashVal]
        shift = pre.next   
        
        if shift is None:
            pre.link(newNode)
            newNode.link(shift)
            return
                            
        skey = shift.key
        while shift is not None:
            
            if shift.key == key:
                shift.val = value
                break
                
            elif shift.key < key:
                pre = shift
                shift = shift.next
                
            if shift is None or shift.key > key:
                pre.link(newNode)
                newNode.link(shift)
                break
                                        
                
    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hashVal = key % len(self.lst)
        pre = self.lst[hashVal]
        shift = pre.next 
        
        while shift is not None and shift.key <= key:
            if shift.key == key:
                return shift.val
            else:
                shift = shift.next
                
        return -1
        

    def remove(self, key: int) -> None:

        hashVal = key % len(self.lst)
                
        pre = self.lst[hashVal]        
        shift = pre.next 

        while shift is not None and shift.key <= key:
            if shift.key == key:                
                pre.link(shift.next)            
                return
            else:
                pre = shift
                shift = shift.next

        return
                        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
