#110. Balanced Binary Tree
#Given a binary tree, determine if it is height-balanced.

#For this problem, a height-balanced binary tree is defined as:

#a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

 

#Example 1:

#Given the following tree [3,9,20,null,null,15,7]:

#    3
#   / \
#  9  20
#    /  \
#   15   7
#Return true.

#Example 2:

#Given the following tree [1,2,2,3,3,null,null,4,4]:

#       1
#      / \
#     2   2
#    / \
#   3   3
#  / \
# 4   4
#Return false.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def difMaxDepth(node):
            if node is None: return -1
            return max(difMaxDepth(node.right)+1,difMaxDepth(node.left)+1)
        if root is None: return True
        right_dif, left_dif= difMaxDepth(root.right), difMaxDepth(root.left)
        return abs(left_dif- right_dif)<=1 and self.isBalanced(root.left) and self.isBalanced(root.right)