# finding the shortest path -> use bfs
# fastest solution so far:
# since is BFS, once reach the target, it must be the shortest path
# avoid TLE -> is BFS, so every value that has been visitedshould be avoid
# because the shortest path must be parsed before

class Solution:
    
    def coinChange(self, coins: List[int], tgt: int) -> int:
        
        if tgt == 0:
            return 0
        
        curNode = [0, 0, 0]
        stack = [curNode]
        
        memo = set()        
        while len(stack) > 0:
            curSize = len(stack)
            nextStack = []
            for i in range(0, curSize):
                node = stack.pop()
                for j in range(node[2], len(coins)):
                    val = node[0] + coins[j]
                    count = node[1] + 1                                                           
                    if val == tgt:
                        return count
                    if val < tgt and val not in memo:                
                        memo.add(val)
                        nextStack.append([val, count, j])
            stack = nextStack
        
        return -1
            
