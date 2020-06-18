"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if node is None:
            return None
        
        #build adj array:
        _map, visited = dict(), set()
        stack = [node]
        visited.add(node.val)  
        while len(stack) > 0:
            curSize = len(stack)            
            nextStep = []
            for i in range(0, curSize):                            
                n1 = stack.pop() 
                v1= n1.val                              
                _map[v1] = []                            
                for neighbor in n1.neighbors:
                    if neighbor.val not in visited:
                        nextStep.append(neighbor)
                        visited.add(neighbor.val)                        
                    _map[v1].append(neighbor.val)
            stack = nextStep
            
        nodes = [None] * len(_map.keys())
        for key in _map.keys():    
            nodes[key - 1] = Node(key, None)
        
        for i in range(0, len(nodes)):
            for neighbor in _map[i + 1]:
                nodes[i].neighbors.append(nodes[neighbor - 1]) 
                                        
        return nodes[0]
                    
        
