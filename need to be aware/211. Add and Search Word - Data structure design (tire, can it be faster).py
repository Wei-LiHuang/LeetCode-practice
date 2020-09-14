class WordDictionary:
    
    class Node:
        
        def __init__(self, char):
            self.isWord = False
            self.char = char
            self.next = []
            for i in range(0, 26):
                self.next.append(None)
                
        def getChildren(self, index):
            return self.next[index]
                
        def setChild(self, child, index):
            if self.next[index] is None:
                self.next[index] = child
                    
    def __init__(self):
        self.root = self.Node(None)
        
    def addWord(self, word: str) -> None:
        curNode = self.root
        for i in range(0, len(word)):            
            curChar = word[i]
            index = ord(curChar) - ord('a')
            _next = curNode.getChildren(index)
            if _next is None:
                _next = self.Node(curChar)
                curNode.setChild(_next, index)
                curNode = _next
            else:
                curNode = _next
            
            if i == len(word) - 1:
                curNode.isWord = True
                   
    def rec(self, word, index, curNode):        
        
        curChar = word[index]
        
        if curChar == '.':            
            found = False            
            for j in range(0, 26):
                replaceChar = chr(j + ord('a'))
                searchIndex = ord(replaceChar) - ord('a')
                _next = curNode.getChildren(searchIndex)
                if _next is None:
                    continue
                else:
                    if index != len(word) - 1:                                        
                        if self.rec(word, index + 1, _next):
                            found = True
                            break
                    else:
                        if _next.isWord:
                            found = True
                            break            
            return found
                    
        else:
            searchIndex = ord(curChar) - ord('a')
            _next = curNode.getChildren(searchIndex)
            if _next is None:
                return 
            else:
                if index != len(word) - 1:
                    return self.rec(word, index + 1, _next)
                else:
                    return _next.isWord
            
                    
    def search(self, word: str) -> bool:
        curNode = self.root
        return self.rec(word, 0, curNode)


            
