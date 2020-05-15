# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# palindrome: "aba", "aa", ""
# brute force: traverse all list get the whole string then check is palindrome
# run time: traverse: O(n), check Palindrome: O(n) -> O(n)

class Solution(object):
    
    def getString (self, cur, lst):        
        if cur is None:
            return        
        lst.append(cur.val)
        self.getString(cur.next, lst)
        return
    
    def checkPalindrome(self, lst):
        size = len(lst)
        i = 0
        j = size - 1
        
        while i <= j:
            if lst[i] != lst[j]:
                return False
            else:
                i += 1
                j -= 1
        
        return True
        
            
    def isPalindrome(self, head):
        lst = []
        self.getString(head, lst)
        return self.checkPalindrome(lst)
