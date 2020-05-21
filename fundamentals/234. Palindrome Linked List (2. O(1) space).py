# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# 1.
# palindrome: "aba", "aa", ""
# brute force: traverse all list get the whole string then check is palindrome
# run time: traverse: O(n), check Palindrome: O(n) -> O(n)

# 2.
# use O(1) space: traverse to the end of the list, then start popping back
# while popping back, use p2 = head to traverse to the end, check palindrome
# should only need to check the half of the list -> add a counter to see when to stop

class Solution(object):
        
    def isPalindrome(self, head):                            
        
        self.p2 = head

        def rec(p1):
            if p1 is not None:        
                if not rec(p1.next):
                    return False

            elif p1 is None:
                return True

            v1 = p1.val
            v2 = self.p2.val
            if v1 != v2:
                return False
            else:
                self.p2 = self.p2.next
                return True
            
        
        p1 = head
        return rec(p1)
