#1290. Convert Binary Number in a Linked List to Integer
#Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

#Return the decimal value of the number in the linked list.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
#         ## queue/stack
#         stored =[]
#         while head is not None:
#             stored.append(head.val)
#             head = head.next
            
#         out = 0
#         while stored:
#             cur_num = stored.pop(0)
#             out+=cur_num* (2**len(stored))
        
#         return out
        
        
        
        
        
        ##two time traversal:
        ## first get the total length and then calculate the sum recursively
        ## O(n) space recursively, O(1) iteratively
        
        l=0
        temp = head
        while temp:
            l+=1
            temp= temp.next
            
        out, cur_i = 0, 1
        while head:
            out += head.val*(2**(l-cur_i))
            cur_i+=1
            head = head.next
        return out
            
        
#         def traverse(node, l, cur_i):
#             if not node:
#                 return 0
#             return node.val*(2**(l-cur_i))+traverse(node.next, l, cur_i+1)

#         return traverse(head, l, 1)
        
        
        
        
        
        
        