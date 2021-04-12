#538. Convert BST to Greater Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        ## binary search tree
        ## inorder traversal from right to left
        ## O(n), O(n)
        self.cum_sum=0
        def traverse(node):
            if not node: return
            traverse(node.right)
            self.cum_sum+=node.val
            node.val = self.cum_sum
            traverse(node.left)

        traverse(root)
        return root
