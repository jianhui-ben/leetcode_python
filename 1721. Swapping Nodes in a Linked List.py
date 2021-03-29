#1721. Swapping Nodes in a Linked List
#You are given the head of a linked list, and an integer k.

#Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).
#Input: head = [1,2,3,4,5], k = 2
#Output: [1,4,3,2,5]


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        
        ## convert into array and traverse twice
        ## time O(n), space O(1)
        left, right=head, head
        for _ in range(k-1):
            right=right.next
        save= right.val
        
        ## two pointer
        while right.next:
            right=right.next
            left=left.next
        new_save= left.val
        left.val=save
        
        new_head= head
        for _ in range(k-1):
            new_head=new_head.next
            
        new_head.val=new_save
        
        return head
        