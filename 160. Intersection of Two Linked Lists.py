#160. Intersection of Two Linked Lists

#Write a program to find the node at which the intersection of two singly linked lists begins.

#For example, the following two linked lists:
#begin to intersect at node c1.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


## very intersting two pointer problems
##  two pointers: 
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None: return None
        a, b= headA, headB
        while a!= b:
            if a is None:
                a=headB
            else: a=a.next
            
            if b is None: 
                b=headA
            else: b= b.next
                
        return a