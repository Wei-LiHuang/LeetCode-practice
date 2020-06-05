class Solution:
        
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
                            
        def getStopPoints(maze, curR, curC, visited):
            
            row = len(maze)
            col = len(maze[0])
            
            curIndex = curR * col + curC
            
            if curIndex in visited:
                return []
                        
            visited.add(curIndex)
            
            neighbors = []
            
            # go left:
            leftC = curC
            while leftC > 0 and maze[curR][leftC - 1] != 1:
                leftC -= 1
                
            leftMostStop = curR * col + leftC
            if leftMostStop not in visited:
                neighbors.append(leftMostStop)
                
            # go right:
            rightC = curC
            while rightC < col - 1 and maze[curR][rightC + 1] != 1:
                rightC += 1
                
            rightMostStop = curR * col + rightC
            if rightMostStop not in visited:
                neighbors.append(rightMostStop)
                
                
            # go Down:
            downR = curR
            while downR < row - 1 and maze[downR + 1][curC] != 1:
                downR += 1
            downMostStop = downR * col + curC
            if downMostStop not in visited:
                neighbors.append(downMostStop)
                
            # go up:
            upR = curR
            while upR > 0 and maze[upR - 1][curC] != 1:
                upR -= 1
            upMostStop = upR * col + curC
            if upMostStop not in visited:
                neighbors.append(upMostStop)           
                
            return neighbors
                
        m = len(maze)
        if m == 0:
            return True
        
        n = len(maze[0])
        if n == 0:
            return True
                        
        startPoint = start[0] * n + start[1]        
        visited, stack = set(), [startPoint]
        
        while len(stack) != 0:            
            nextStep, size = [], len(stack)
            
            for i in range(0, size):
                cur = stack.pop()
                curR = cur // n
                curC = cur % n
                
                if curR == destination[0] and curC == destination[1]:
                    return True
                
                neighbors = getStopPoints(maze, curR, curC, visited)
                nextStep.extend(neighbors)
            
            stack = nextStep
            
        return False
                
            
                
            
