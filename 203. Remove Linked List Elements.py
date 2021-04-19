#203. Remove Linked List Elements


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        ## iterative with extra head
        new_head= ListNode(0)
        prev, cur= new_head, head
        while cur:
            if cur.val==val:
                prev.next= cur.next
            else:
                prev.next = cur
                prev=prev.next
            cur=cur.next
        return new_head.next
                

        ## iterative:
        new_head, pre_tail, cur_node = None, None, head
        while cur_node:
            if cur_node.val!=val:
                if pre_tail:
                    pre_tail.next = cur_node
                pre_tail = cur_node
                if not new_head:
                    new_head= cur_node
            elif pre_tail:
                pre_tail.next=cur_node.next
            cur_node = cur_node.next
        return new_head

        
        
        ## recursion O(n), O(n)
        if not head:
            return None
        if head.val ==val:
            return self.removeElements(head.next, val)
        else:
            head.next = self.removeElements(head.next, val)
            return head
            
        
