#100. Same Tree
#Given two binary trees, write a function to check if they are the same or not.

#Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

#Example 1:

#Input:     1         1
#          / \       / \
#         2   3     2   3

#        [1,2,3],   [1,2,3]

#Output: true

#Example 2:

#Input:     1         1
#          /           \
#         2             2

#        [1,2],     [1,null,2]

#Output: false


## I want to try with recursion
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## time complexity: O(n)
## space complexity: O(log n) for balanced tree; O(n) for worst case unbalanced tree
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def test_node(p, q):
            if p is None and q is None:
                return True
            elif (p is None and q is not None) or (q is None and p is not None) :
                return False
            elif p.val!= q.val:
                return False
            return test_node(p.left, q.left) and test_node(p.right, q.right)
        return test_node(p,q) 


## iterative method:
from collections import deque
class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """    
        def check(p, q):
            # if both are None
            if not p and not q:
                return True
            # one of p and q is None
            if not q or not p:
                return False
            if p.val != q.val:
                return False
            return True
        
        deq = deque([(p, q),])
        while deq:
            p, q = deq.popleft()
            if not check(p, q):
                return False
            
            if p:
                deq.append((p.left, q.left))
                deq.append((p.right, q.right))
                    
        return True