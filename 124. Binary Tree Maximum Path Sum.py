#124. Binary Tree Maximum Path Sum
#A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

#The path sum of a path is the sum of the node's values in the path.

#Given the root of a binary tree, return the maximum path sum of any path.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        ## post traversal
        ## time O(N), space O(H) for balanced tree, O(N)for worst case
        out = float('-inf')
        
        def traverse(node): ## return the max path from node
            if not node: return 0
            nonlocal out
            left_l, right_l = traverse(node.left), traverse(node.right)
            out= max([out, node.val, 
                     node.val+left_l, node.val+right_l, \
                     node.val+left_l+right_l])
            return max([node.val+left_l, node.val+right_l, node.val])

        traverse(root)
        
        return out
        
        