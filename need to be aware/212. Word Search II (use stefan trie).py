# from Ryan

# 1. build trie
# 2. do dfs
# 3. need to avoid going back -> modify b[r][c]
# 4. need to change the isWord Val in trie nodes after adding into result
# 5. follow the board and the trie path, only traverse the path in the trie

class Solution:
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:            
        
        def buildDict(words):
            root = dict()
            for w in words:                
                shift = root
                for c in w:
                    if c in shift:
                        shift = shift[c]
                    else:
                        shift[c] = dict()
                        shift = shift[c]                                      
                shift[None] = None
                                      
            #print(root)
            return root
        
        def dfs(b, r, c, node, path, res):
            
            path += b[r][c]
                           
            if None in node:
                # need to remember1: del isWord flag
                del node[None]
                res.append(path)   
                
                # need to remember2: shouldn't return
                #return                        
            
            # need to remember3: avoid backward
            temp = b[r][c]
            b[r][c] = ' '
            
            m, n = len(b), len(b[0])
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for d in directions:
                nr, nc = r + d[0], c + d[1]
                if nr >= 0 and nr < m and nc >= 0 and nc < n:                    
                    if b[nr][nc] in node:
                        dfs(b, nr, nc, node[b[nr][nc]], path, res)                            
                        
            
            b[r][c] = temp
                            
            return
                                        
        root = buildDict(words)
        m, n = len(board), len(board[0])
        
        res = []
        for i in range(0, m):
            for j in range(0, n):
                if board[i][j] in root:
                    c = board[i][j]
                    dfs(board, i, j, root[c], "", res)
                    
        return res
