# from Ryan

# 1. build trie
# 2. do dfs
# 3. need to avoid going back -> modify b[r][c]
# 4. need to change the isWord Val in trie nodes after adding into result
# 5. follow the board and the trie path, only traverse the path in the trie

class Solution:   
                
    class Trie:        
        
        class Node:
            def __init__(self):
                self.isWord = False
                self.children = [None] * 26
                self.val = ""        
        
        def __init__(self):
            self.root = self.Node()
        
        def setWord(self, word):
            shift = self.root
            for i in range(0, len(word)):
                cIndex = ord(word[i]) - ord('a')                
                if shift.children[cIndex] is None:
                    shift.children[cIndex] = self.Node()                
                if i == len(word) - 1:
                    shift.children[cIndex].isWord = True
                    shift.children[cIndex].val = word
                else:
                    shift = shift.children[cIndex]
                                                            
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        def dfs(board, r, c, tNode, res):
            
            if tNode.isWord:
                res.append(tNode.val)
                tNode.val = ""
                tNode.isWord = False
                                            
            m, n = len(board), len(board[0])
            
            temp = board[r][c]
            board[r][c] = ' '
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            
            for d in directions:
                nr = r + d[0]
                nc = c + d[1]                
                if nr >= 0 and nr < m and nc >= 0 and nc < n and board[nr][nc] != ' ':
                    curChar = board[nr][nc]
                    index = ord(curChar) - ord('a')
                    if tNode.children[index] is not None:
                        dfs(board, nr, nc, tNode.children[index], res)
                        
            board[r][c] = temp
                                                                    
        m = len(board)
        if m == 0:
            return []
        
        n = len(board[0])
        
        trie = self.Trie()        
        for word in words:
            trie.setWord(word)
            
        res = []
        
        for r in range(0, m):
            for c in range(0, n):
                curChar = board[r][c]
                curTrieIndex = ord(curChar) - ord('a')
                if trie.root.children[curTrieIndex] is not None:
                    dfs(board, r, c, trie.root.children[curTrieIndex], res)
                    
        return res
                
