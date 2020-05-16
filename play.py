class Node(object):
    
    def __init__(self, val, pre, nxt):
        self.nxt = nxt
        self.pre = pre
        self.val = val
        
    
    def moveToHead(self, head):
        if self.pre is not None:
            self.pre.nxt = self.nxt
            if self.nxt is not None:
                self.nxt.pre = self.pre
        self.nxt = head 
        self.pre = None
        return self


def createList():

    head = None
    
    for i in range(0, 10):
        node = Node(i, None, None)
        if i != 0:
            print("b\n")
            head.pre = node
            head = node.moveToHead(head)
        else:
            print("a\n")
            head = node

    shift = head
    for i in range(0, 10):
        print(shift.val)
        print("\n")
        shift = shift.nxt



createList()
