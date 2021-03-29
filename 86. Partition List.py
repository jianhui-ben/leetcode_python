#86. Partition List
#Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

#You should preserve the original relative order of the nodes in each of the two partitions.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        ## two pointers
        ## one for before x and one for greater or equal to x
        ## O(n) time and space
        before_head, after_head= ListNode(), ListNode()
        before, after = before_head, after_head
        while head:
            if head.val<x:
                before.next=ListNode(head.val)
                before=before.next
            else:
                after.next=ListNode(head.val)
                after=after.next                
            head=head.next
            
        before.next=after_head.next
        return before_head.next