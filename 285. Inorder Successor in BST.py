# 285. Inorder Successor in BST
# Given the root of a binary search tree and a node p in it, return the in-order successor of that node in the BST. If the given node has no in-order successor in the tree, return null.
#
# The successor of a node p is the node with the smallest key greater than p.val.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'Optional[TreeNode]':
        self.out = None

        def recursion(cur_node, p):
            if not cur_node: return
            if cur_node.val < p.val:
                recursion(cur_node.right, p)
            elif cur_node.val > p.val:
                self.out = cur_node
                recursion(cur_node.left, p)
            elif cur_node.val == p.val and cur_node.right:
                temp = cur_node.right
                while temp.left:
                    temp = temp.left
                self.out = temp

        recursion(root, p)
        return self.out