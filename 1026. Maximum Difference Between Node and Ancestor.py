# 1026. Maximum Difference Between Node and Ancestor
# Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.
#
# A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        """
        post order traversal to return min and max under a child
        """
        self.out = float('-inf')

        def traverse(node):
            if not node: return (float('inf'), float('-inf'))
            if not node.left and not node.right: return (node.val, node.val)
            left_min, left_max = traverse(node.left)
            right_min, right_max = traverse(node.right)
            self.out = max(self.out, max(abs(node.val - min(left_min, right_min)), \
                                         abs(node.val - max(left_max, right_max))))

            return (min(left_min, right_min, node.val), max(left_max, right_max, node.val))

        traverse(root)

        return self.out