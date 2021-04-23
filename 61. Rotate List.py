#61. Rotate List
#Given the head of a linked list, rotate the list to the right by k places.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        ##get the length first
        
        if not head: return head
        l=0
        temp= head
        while temp:
            l+=1
            temp=temp.next
        if l<=1: return head
        k=k%l
        if not k: return head
        move_to_right=l-k
        ## iterative
        if not move_to_right: return head
        left_head, cur = head, head

        while move_to_right>1:
            cur = cur.next
            move_to_right-=1
        
        right_head =cur.next
        cur.next = None
        
        cur = right_head
        while cur.next:
            cur = cur.next
            
        cur.next = left_head
        
        return right_head
            
        
        