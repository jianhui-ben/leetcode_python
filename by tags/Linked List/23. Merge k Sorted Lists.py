#23. Merge k Sorted Lists
#You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

#Merge all the linked-lists into one sorted linked-list and return it.

 

#Example 1:

#Input: lists = [[1,4,5],[1,3,4],[2,6]]
#Output: [1,1,2,3,4,4,5,6]
#Explanation: The linked-lists are:
#[
#  1->4->5,
#  1->3->4,
#  2->6
#]
#merging them into one sorted list:
#1->1->2->3->4->4->5->6


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

## time O(nlogn), space O(n)
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        lists= [i for i in lists if i]
        if not lists: return None
        new_head= ListNode()
        cur_node=new_head
        while lists:
            lists.sort(key=lambda node: node.val)
            cur_list_node= lists.pop(0)
            cur_node.next= ListNode(cur_list_node.val)
            cur_node=cur_node.next
            cur_list_node=cur_list_node.next
            if cur_list_node:
                lists.append(cur_list_node)
        return new_head.next
            