#226. Invert Binary Tree
#Invert a binary tree.

#Example:

#Input:

#     4
#   /   \
#  2     7
# / \   / \
#1   3 6   9
#Output:

#     4
#   /   \
#  7     2
# / \   / \
#9   6 3   1


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root: return None
        if not root.left and not root.right: return root
        # if root.left and not root.right: 
        #     root.right=root.left
        #     root.left=None
        #     return root
        # if root.right and not root.left: 
        #     root.left=root.right
        #     root.right=None
        #     return root
        temp=root.left
        root.left=self.invertTree(root.right)
        root.right= self.invertTree(temp)
        return root
