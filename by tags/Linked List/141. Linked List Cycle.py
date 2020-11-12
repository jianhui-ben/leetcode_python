#141. Linked List Cycle

#Given a linked list, determine if it has a cycle in it.

#To represent a cycle in the given linked list, we use an integer pos which represents 
#the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

 

#Example 1:

#Input: head = [3,2,0,-4], pos = 1
#Output: true
#Explanation: There is a cycle in the linked list, where tail connects to the second node.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


## hash table space complexity: O(n)
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        hash= set()
        while head:
            if head in hash: return True
            else: hash.add(head)
            head=head.next
        return False


## two pointers with different speeds, space complexity: O(1)
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next: return False
        first, second = head, head.next
        while first!= second:
            if (second.next is None) or (second.next.next is None): return False
            first, second= first.next, second.next.next
        return True