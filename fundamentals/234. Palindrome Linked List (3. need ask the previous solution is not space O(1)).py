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
# this is actually not O(1), the stack still got two node ptr?

class Solution(object):
        
    def isPalindrome(self, head):
        arr = []
        shift = head
        while shift is not None:
            arr.append(shift.val)
            shift = shift.next
            
        left, right = 0,  len(arr) - 1
        
        while left < right:
            if arr[left] != arr[right]:
                return False
            
            left += 1
            right -= 1
        
        
        return True
        

        
                
