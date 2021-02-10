#143. Reorder List
#Given a singly linked list L: L0→L1→…→Ln-1→Ln,
#reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

#You may not modify the values in the list's nodes, only nodes itself may be changed.

#Example 1:

#Given 1->2->3->4, reorder it to 1->4->2->3.
#Example 2:

#Given 1->2->3->4->5, reorder it to 1->5->2->4->3.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next: return head
        
        stored_node=[]    
        cur_node= head
        while cur_node:
            stored_node.append(cur_node)
            cur_node= cur_node.next
        empty_head= ListNode()
        cur_node= empty_head
        for i in range(len(stored_node)//2):
            cur_node.next= stored_node[i]
            stored_node[i].next= stored_node[-(i+1)]
            cur_node=cur_node.next.next
        if len(stored_node)%2==0: cur_node.next= None
        else: 
            cur_node.next= stored_node[len(stored_node)//2]
            cur_node.next.next=None
        return stored_node[0]
        
        
##second method to save some space
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head
        
        # find mid point
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        # reverse from mid point
        reverse = None
        while slow:
            cur = slow
            slow = slow.next
            cur.next = reverse
            reverse = cur
            
        # mix reverse and head
        pointHead = head
        pointRev = reverse
        while pointHead:
            tempHead = pointHead.next
            pointHead.next = pointRev
            pointRev = tempHead
            pointHead = pointHead.next        
