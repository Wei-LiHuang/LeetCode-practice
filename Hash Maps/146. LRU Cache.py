# for O(1) check is a node exist in cache: hash set
# for O(1) remove tail: need a linked list tail node
# for O(1) insert head: need a linked list head node => so we also need a double sided linked list

class LRUCache(object):
    
    class Node(object):
        def __init__(self, val, key, right, left):
            self.val = val
            self.key = key
            self.right = right
            self.left = left
            
    def __init__(self, capacity):
        self.cap = capacity
        self.curSize = 0
        self.head = None
        self.tail = None
        self._dict = dict()
        
    def removeNode(self, node):        
        if self.curSize == 0:
            return;
        
        if self.curSize == 1 and node is self.head and node is self.tail:
            self.head = None
            self.tail = None
            self.curSize = 0
            self._dict.pop(node.key)
            return
        
        # size >= 2:
        if node is self.head or node is self.tail:
            if node is self.head:
                self.head = self.head.right
                self.head.left = None
            if node is self.tail:
                self.tail = self.tail.left
                self.tail.right = None                                                
            self._dict.pop(node.key)
            self.curSize -= 1
            return
        
        node.left.right = node.right
        node.right.left = node.left
        self._dict.pop(node.key)
        self.curSize -= 1
        return                
    def addToHead(self, node):
        
        if self.curSize == 0:
            self.head = node
            self.tail = node
            self._dict[node.key] = node
            self.curSize = 1
            return
        
        if node is self.head:
            return
        
        if self.curSize == 1:
            node.right = self.head
            self.head.left = node
            self.head = node        
            self._dict[node.key] = node
            self.curSize = 2
            return
                        
        # size >= 2:
        if node is self.tail:
            self.tail.left.right = None
            self.tail = self.tail.left #node change also?
            node.right = None
            node.left = None
        
        node.right = self.head
        self.head.left = node
        self.head = node        
        self._dict[node.key] = node   
        self.curSize += 1
        return    
            
        
    def get(self, key):
        if key in self._dict:
            node = self._dict.get(key)
            self.removeNode(node)
            self.addToHead(node)
            return node.val
        else:
            return -1
                                
    def put(self, key, value):
        if key in self._dict:
            node = self._dict.get(key)
            node.val = value
            self.removeNode(node)
            self.addToHead(node)
            return            
        else:
            node = self.Node(value, key, None, None)
            self.addToHead(node)
            if self.curSize > self.cap:
                self.removeNode(self.tail)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
