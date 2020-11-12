
#Merge two sorted linked lists and return it as a new sorted list. 
#The new list should be made by splicing together the nodes of the first two lists.

#Example:

#Input: 1->2->4, 1->3->4
#Output: 1->1->2->3->4->4

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head= ListNode()
        next= head
        while l1 and l2:
            if l1.val< l2.val:
                next.next= ListNode(l1.val)
                l1=l1.next
            else:
                next.next=ListNode(l2.val)
                l2=l2.next
            next=next.next
        if l1:
            next.next=l1
        if l2:
            next.next= l2
        return head.next

