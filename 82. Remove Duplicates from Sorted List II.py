#82. Remove Duplicates from Sorted List II
#Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        ## sorted 
        ## O(n) , O(1)
        new_head = ListNode(0, head)
        cur = new_head
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val ==head.next.val:
                    head=head.next
                cur.next = head.next
            else:
                cur= cur.next

            head = head.next
        return new_head.next
            
        
        
        
        
        
        
        
        ## hashtable O(n) space O(n)
        store =defaultdict(int)
        
        temp =head
        while temp:
            store[temp.val]+=1
            temp = temp.next
        prev, cur = ListNode(), head
        new_head = prev
        while cur:
            prev.next = None
            if store[cur.val]==1:
                prev.next = cur
                prev = prev.next
                cur = cur.next
            else:
                cur=cur.next
        return new_head.next
                