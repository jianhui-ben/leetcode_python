#111. Minimum Depth of Binary Tree

#Given a binary tree, find its minimum depth.

#The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

#Note: A leaf is a node with no children.

#Example:

#Given binary tree [3,9,20,null,null,15,7],

#    3
#   / \
#  9  20
#    /  \
#   15   7
#return its minimum depth = 2.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## time complexity: O(n); space complexity: O(log n) on average
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None: return 0
        def minLeaf(node):
            if node.right is None and node.left is None: return 1
            if node.right is None: return 1+ minLeaf(node.left)
            if node.left is None: return 1+minLeaf(node.right)
            return min(minLeaf(node.left), minLeaf(node.right))+1
        return minLeaf(root)
