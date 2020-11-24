#104. Maximum Depth of Binary Tree
#Given a binary tree, find its maximum depth.

#The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

#Note: A leaf is a node with no children.

#Example:

#Given binary tree [3,9,20,null,null,15,7],

#    3
#   / \
#  9  20
#    /  \
#   15   7
#return its depth = 3.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## recursion: time complexity: O (n); space complexity: O(n log n) on average for balanced tree O(n) in worst case unbalanced tree
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def maxDepth_recursion(node):
            if node is None: return 0
            return max(maxDepth_recursion(node.right)+1, maxDepth_recursion(node.left)+1)
        return maxDepth_recursion(root)

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None: return 0
        return max(self.maxDepth(root.right)+1, self.maxDepth(root.left)+1)