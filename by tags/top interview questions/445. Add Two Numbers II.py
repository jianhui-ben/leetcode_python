#445. Add Two Numbers II
#You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

#You may assume the two numbers do not contain any leading zero, except the number 0 itself.

#Follow up:
#What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

#Example:

#Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
#Output: 7 -> 8 -> 0 -> 7


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,l):
        if not l: 
            return l
        else:
            first, second=l, l.next
            cur= ListNode(first.val)
            cur.next=None
            while second:
                temp=cur
                cur=ListNode(second.val)
                cur.next=temp
                second=second.next
            return cur        
    
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ## approach 1:reverse both and then add
        ##if not reverse input
        
        len_1, len_2=0, 0
        temp1, temp2=l1,l2
        while temp1 or temp2:
            if temp1:
                len_1+=1
                temp1=temp1.next
            if temp2:
                len_2+=1
                temp2=temp2.next
        start=ListNode()
        cur_node=start
        temp1, temp2=l1,l2
        dif= abs(len_2-len_1)
        if len_1>=len_2: 
            for _ in range(dif):
                cur_node.next= ListNode(temp1.val)
                cur_node= cur_node.next
                temp1=temp1.next
        else:
            for _ in range(dif):
                cur_node.next= ListNode(temp2.val)
                cur_node= cur_node.next
                temp2=temp2.next
        while temp1 and temp2:
            cur_node.next= ListNode(temp1.val+temp2.val)
            cur_node=cur_node.next
            temp1=temp1.next
            temp2= temp2.next
        ##next we reverse the list
        reverse_sum= self.reverse(start.next)
        
        ## take care of carry on:
        start, carry_on= ListNode(), 0
        temp= start
        while reverse_sum:
            value= reverse_sum.val+carry_on
            if value>9:
                carry_on=1
            else:
                carry_on=0
            temp.next= ListNode((value)%10)
            temp= temp.next
            reverse_sum=reverse_sum.next
        if carry_on==1: temp.next=ListNode(1)
        # return start.next
        return self.reverse(start.next)
