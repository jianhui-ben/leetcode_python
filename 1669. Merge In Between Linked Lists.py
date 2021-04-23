#1669. Merge In Between Linked Lists


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        ## iterative
        ## O(n), O(1)
        
        ##psedo_head
        new_head = ListNode()
        new_head.next =list1 
        cur = new_head
        
        i = 0
        
        while i<a:
            i+=1
            cur = cur.next
        
        if cur.next:
            remove_start = cur.next
        
        cur.next = list2
        while cur.next:
            cur = cur.next
            
        for _ in range(b-a):
            remove_start= remove_start.next
        
        if remove_start and remove_start.next:
            cur.next =remove_start.next
            
        return new_head.next
        
        
