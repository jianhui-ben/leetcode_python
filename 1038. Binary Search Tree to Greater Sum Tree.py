#1038. Binary Search Tree to Greater Sum Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        ## inorder traversal from right to left:
        self.cum_sum=0
        def traverse(node):
            
            if not node: return 
            traverse(node.right)
            self.cum_sum+=node.val
            node.val = self.cum_sum
            traverse(node.left)

        traverse(root)
        
        return root
        