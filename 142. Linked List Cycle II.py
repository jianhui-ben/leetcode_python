#142. Linked List Cycle II

#Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

#There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

#Notice that you should not modify the linked list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        ## two pointer
        fast, slow =  head, head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            if fast == slow:
                break
        if not fast or not fast.next:
            return None
        
        new = head
        while new!= slow:
            new = new.next
            slow = slow.next
        return new
            