#430. Flatten a Multilevel Doubly Linked List
#You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.

#Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.


"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        ## recursive DFS preorder traversal
        
        out_node = Node(0)
        cur_node = out_node
        def traverse(node):
            nonlocal cur_node
            if not node: return node
            cur_node.next=node
            node.prev = cur_node
            cur_node = node
            stored_next = node.next
            if node.child:
                traverse(node.child)
            traverse(stored_next)
        
        traverse(head)
        
        return out_node.next
                
        