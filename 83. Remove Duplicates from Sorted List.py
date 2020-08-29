#83. Remove Duplicates from Sorted List
#Given a sorted linked list, delete all duplicates such that each element appear only once.

#Example 1:

#Input: 1->1->2
#Output: 1->2
#Example 2:

#Input: 1->1->2->3->3
#Output: 1->2->3

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


## pay attention: it's a sorted linked list
## if not, we would either create a remove function or use two while loop to do


## time complexity: O(n)
## space complexity: O(1); in-place
def deleteDuplicates(head: ListNode) -> ListNode:
    cur_node= head
    while cur_node and cur_node.next:
        if cur_node.val==cur_node.next.val:
            cur_node.next= cur_node.next.next
        else: cur_node=cur_node.next
    return head 