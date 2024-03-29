#617. Merge Two Binary Trees


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        ##pre-order traversal
        ## time O(min(N1, N2)), space O(min(N1, N2))
        if not root1 and not root2:
            return None
        elif not root1:
            return root2
        elif not root2:
            return root1
        
        root = TreeNode(root1.val+root2.val)
        root.left= self.mergeTrees(root1.left, root2.left)
        root.right= self.mergeTrees(root1.right, root2.right)
        
        return root
        
