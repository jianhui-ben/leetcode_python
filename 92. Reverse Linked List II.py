#92. Reverse Linked List II
#Given the head of a singly linked list and two integers left and right where left 
#<= right, reverse the nodes of the list from position left to position right, and 
#return the reversed list.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        ##recursion
        ## O(n) time, O(n) space
        after_reverse=None
        def reverse(head, n):
            nonlocal after_reverse
            if n==1:
                after_reverse=head.next
                return head
            last = reverse(head.next, n-1)
            head.next.next=head
            head.next = after_reverse
            return last
        
        if left==1:
            return reverse(head, right)
        else:
            head.next=self.reverseBetween(head.next, left-1, right-1)
            return head
        



