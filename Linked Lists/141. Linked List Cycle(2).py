# if the list has cycle => fast will catech up eventually
# so the slow and fast can all be set to the head at the begining as long as the step is different
# (but needs to add a condiction slow is fast and slow is not head in line 23)
# the fast can also taking three step at each loop, but need to be careful to the consequences using this in len = 2 list.

class Solution(object):

    def hasCycle(self, head):
        
        if head is None or head.next is None:
            return False
        
        slow = head
        fast = head.next
        
        while fast != None:
            if slow is fast:
                return True
            else:
                slow = slow.next
                fast = fast.next
                if fast is None:
                    return False
                fast = fast.next
                            
        return False
