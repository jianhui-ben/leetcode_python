#117. Populating Next Right Pointers in Each Node II


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
        ## should also try BFS to do so 
        
        
        
        ## brute recursion
        ## pre order from right to left
        ## time O(N * width), space O(1)
        if not root:
            return None
        if root.left:
            if root.right:
                root.left.next = root.right
            else:
                temp=root
                while temp.next and not root.left.next:
                    if temp.next.left:
                        root.left.next = temp.next.left
                    elif temp.next.right:
                        root.left.next = temp.next.right
                    temp= temp.next

        if root.right:
            temp=root
            while temp.next and not root.right.next:

                if temp.next.left:
                    root.right.next = temp.next.left
                elif temp.next.right:
                    root.right.next = temp.next.right
                temp= temp.next

        self.connect(root.right)
        self.connect(root.left)
        return root
        
        
