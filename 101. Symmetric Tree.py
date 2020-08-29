
#101. Symmetric Tree
#Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

#For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

#    1
#   / \
#  2   2
# / \ / \
#3  4 4  3
 

#But the following [1,2,2,null,3,null,3] is not:

#    1
#   / \
#  2   2
#   \   \
#   3    3

#Follow up: Solve it both recursively and iteratively.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## iterative approach
from collections import deque
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def check(a, b):
            if a is None and b is None: return True
            elif a is None or b is None: return False
            elif a.val != b.val: return False
            return True
        if root is None: return True
        queue=deque([(root.left, root.right), ])
        while queue:
            left, right= queue.popleft()
            if not check(left, right):
                return False
            if  left:
                queue.append((left.left, right.right))
                queue.append((left.right, right.left))
        return True


## recursive:
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None: return True
        def check(left, right):
            if left is None and right is None: return True
            elif left is None or right is None: return False
            elif left.val!= right.val: return False
            return check(left.left, right.right) and check(left.right, right.left)
        return check(root.left,root.right)

            