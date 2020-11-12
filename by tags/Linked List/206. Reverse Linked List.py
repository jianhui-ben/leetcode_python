#206. Reverse Linked List
#Reverse a singly linked list.

#Example:

#Input: 1->2->3->4->5->NULL
#Output: 5->4->3->2->1->NULL
#Follow up:

#A linked list can be reversed either iteratively or recursively. Could you implement both?


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    ##iterative method: O(n)
    # def reverseList(self, head: ListNode) -> ListNode:
    #     if not head: return None
    #     cur_node= head
    #     nextOne=cur_node.next
    #     cur_node.next= None
    #     while nextOne:
    #         temp = nextOne.next
    #         nextOne.next= cur_node
    #         cur_node=nextOne
    #         nextOne=temp
    #     return cur_node
    
    ##recursive method: very smart 
    def reverseList(self, head: ListNode) -> ListNode:
        if not head: return None
        if not head.next: return head
        new_head= self.reverseList(head.next)
        head.next.next= head
        head.next= None
        return new_head
        