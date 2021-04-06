#114. Flatten Binary Tree to Linked List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        ## tree traversal
        ## O(n), space O(n)         
        
        if not root:
            return
        
        self.flatten(root.left)
        self.flatten(root.right)
        
        cur_left= root.left
        while cur_left and cur_left.right:
            cur_left=cur_left.right
        if cur_left:
            cur_left.right = root.right
            root.right=root.left
            root.left = None
            
            
        ## iterative O(1) space traversal is tricky
        
        
        