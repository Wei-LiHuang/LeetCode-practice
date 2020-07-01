    def sortedListToBST(self, head: ListNode):
        
        if head is None:
            return None
        
        nodes = []
        shift = head        
        while shift is not None:            
            nodes.append(shift.val)
            shift = shift.next

        arr = []
        stack = collections.deque()
        stack.append([0, len(nodes) - 1])            
        while len(stack) > 0:
            curSize = len(stack)

            for i in range(0, curSize):
                
                region = stack.pop()
                if region is None:
                    arr.append(None)
                    continue
                                
                l, r = region[0], region[1]
                mid = (l + r) // 2
                arr.append(nodes[mid])
                #print(arr)

                if (mid - 1) >= l:
                    stack.appendleft([l, mid - 1])
                else:
                    stack.appendleft(None)                
                
                if mid + 1 <= r:
                    stack.appendleft([mid + 1, r])
                else:
                    stack.appendleft(None)
                                
            
        #print(arr)        
        arr[0] = TreeNode(arr[0])
        for i in range(0, len(arr)):            
            
            if arr[i] is None:
                continue
            
            lIndex, rIndex = i * 2 + 1, i * 2 + 2
            
            if lIndex < len(arr) and arr[lIndex] is not None:
                arr[lIndex] = TreeNode(arr[lIndex])
                arr[i].left = arr[lIndex]
            else:
                arr[i].left = None
            
            if rIndex < len(arr) and arr[rIndex] is not None:
                arr[rIndex] = TreeNode(arr[rIndex])  
                arr[i].right = arr[rIndex]
            else:
                arr[i].right = None
        
        
        return arr[0]
