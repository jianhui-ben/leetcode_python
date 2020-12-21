2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ##brute force
        carry_on=0
        start= ListNode()
        temp=start
        while l1 or l2:
            if l1: a1=l1.val
            else: a1=0
            if l2: a2=l2.val
            else: a2=0
            sums=a1+a2+carry_on
            if sums<10:
                temp.next= ListNode(sums)
                carry_on=0
            else:
                temp.next= ListNode(sums%10)
                carry_on=1
            temp=temp.next
            if l1: l1=l1.next
            if l2: l2=l2.next
        
        if carry_on==1:
            temp.next= ListNode(1)
        
        return start.next
    
                
