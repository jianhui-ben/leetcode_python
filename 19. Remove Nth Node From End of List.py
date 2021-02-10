#19. Remove Nth Node From End of List

#Given the head of a linked list, remove the nth node from the end of 
#the list and return its head.

#Follow up: Could you do this in one pass?


#Example 1:

#Input: head = [1,2,3,4,5], n = 2
#Output: [1,2,3,5]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        ##two pass: space: O(1)
        # length= 0
        # cur_node= head
        # while cur_node:
        #     length+=1
        #     cur_node=cur_node.next
        # cur_node= head
        # if length==n:
        #     return head.next
        # for _ in range(length-n-1):
        #     cur_node=cur_node.next
        # cur_node.next= cur_node.next.next
        # return head
        ##one pass: space O(n)
        store_node=[]
        cur_node= head
        while cur_node:
            store_node.append(cur_node)
            cur_node=cur_node.next
        if len(store_node)==n: return head.next
        if len(store_node)-n+1> len(store_node)-1: store_node[len(store_node)-n-1].next= None
        else: store_node[len(store_node)-n-1].next= store_node[len(store_node)-n+1]
        return head

