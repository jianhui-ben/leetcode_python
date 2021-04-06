#116. Populating Next Right Pointers in Each Node
#You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

#struct Node {
#  int val;
#  Node *left;
#  Node *right;
#  Node *next;
#}
#Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

#Initially, all next pointers are set to NULL.


"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        ## tree traversal
        ## time O(N), space O(n)
        
        ## at every node, we should put its right as the next of its left node
        ## 
        if not root or not root.left or not root.right:
            return root
        root.left.next=root.right
        if root.next:
            root.right.next= root.next.left
        
        self.left = self.connect(root.left)
        self.right = self.connect(root.right)
        
        return root