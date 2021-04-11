#671. Second Minimum Node In a Binary Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        ## O(n), O(n)
        out = []
        if not root: return -1
        # target= root.val
        
        def traverse(node):
            # nonlocal target
            if not node: return
            if node.val >root.val:
                out.append(node.val)
                return
            traverse(node.left)
            traverse(node.right)
        
        traverse(root)
        if not out: return -1
        else: return min(out)
        
        
        
        
        
        
        
        
    
        
        
        
