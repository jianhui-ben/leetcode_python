#234. Palindrome Linked List
#Given a singly linked list, determine if it is a palindrome.

#Example 1:

#Input: 1->2
#Output: false
#Example 2:

#Input: 1->2->2->1
#Output: true
#Follow up:
#Could you do it in O(n) time and O(1) space?



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # if not head: return True
        saved_head= head
        stored= []
        while head:
            stored.append(head.val)
            head=head.next
        
        iteration= len(stored)//2
        for i in range(iteration):
            tail= stored.pop()
            if saved_head.val!= tail:
                return False
            saved_head= saved_head.next
        return True
