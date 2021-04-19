#25. Reverse Nodes in k-Group


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
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        ## O(1) iterative method
        def count_node(node, n):
            cnt=0
            while node:
                cnt+=1
                if cnt==n:
                    return True
                node = node.next
            return False
        def reverse_iterative(node, k):
            new_head, cur_node = None, node
            while k:
                temp = cur_node.next
                cur_node.next = new_head
                new_head= cur_node
                cur_node = temp
                k-=1
            return new_head, cur_node 
        
        cur_node, ktail, new_head = head, None, None
        while count_node(cur_node, k):
            k_head, next_start = reverse_iterative(cur_node, k)
            if not new_head:
                new_head = k_head
            if ktail:
                ktail.next = k_head
            ktail =cur_node
            cur_node = next_start
        
        if ktail and cur_node:
            ktail.next = cur_node
        
        if new_head:
            return new_head
        else:
            return head
        
        
        
        
        
        ## recursion
        ## time O(n), space O(n)
        def count_node(node, n):
            cnt=0
            while node:
                cnt+=1
                if cnt==n:
                    return True
                node = node.next
            return False
        
        # after_one_cycle = None
        # def reverse_recurse(node, n):
        #     nonlocal after_one_cycle
        #     if n==1:
        #         after_one_cycle = node.next
        #         return node
        #     last = reverse_recurse(node.next, n-1)
        #     node.next.next= node
        #     node.next = after_one_cycle
        #     return last
        def reverse_iterative(node, k):
            new_head, cur_node = None, node
            while k:
                temp = cur_node.next
                cur_node.next = new_head
                new_head= cur_node
                cur_node = temp
                k-=1
            return new_head, cur_node
                

        if count_node(head, k):
            new_head, cur_node = reverse_iterative(head, k)
            head.next = self.reverseKGroup(cur_node, k)
        else: new_head = head
            
        return new_head
        
        
    
    
        
        
        
        
        
        
        
        
        
        
