
#572. Subtree of Another Tree
#Given two non-empty binary trees s and t, check whether tree 
#t has exactly the same structure and node values with a subtree of s. 
#A subtree of s is a tree consists of a node in s and all of this node's descendants.
#The tree s could also be considered as a subtree of itself.

#Example 1:
#Given tree s:

#     3
#    / \
#   4   5
#  / \
# 1   2
#Given tree t:
#   4 
#  / \
# 1   2
#Return true, because t has the same structure and node values with a subtree of s.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def equalTree(self, s, t):
        if s==None and t==None: return True
        if s==None or t==None: return False
        if s.val==t.val:
            return self.equalTree(s.left, t.left) \
                and self.equalTree(s.right, t.right)
        


    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if s==None: return False
        if self.equalTree(s,t): return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
