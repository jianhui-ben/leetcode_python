# 1022. Sum of Root To Leaf Binary Numbers
# You are given the root of a binary tree where each node has a value 0 or 1. Each root-to-leaf path represents a binary number starting with the most significant bit.
#
# For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
# For all leaves in the tree, consider the numbers represented by the path from the root to that leaf. Return the sum of these numbers.
#
# The test cases are generated so that the answer fits in a 32-bits integer.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        """
        from binary to int
        '101' -> 1 * 2**0 + 0 * 2 ** 1 + 1 * 2 ** 2 = 5
        fwe
        traverse(root) --> [(current_sum, degree of 2)]
        time: O(n**2), space: O(H + n) --> O(n)
        """

        def traverse(node):
            if not node: return []
            if not node.left and not node.right:
                return [(node.val, 1)]

            out = traverse(node.left) + traverse(node.right)
            return [(cur_sum + 2 ** degree * node.val, degree + 1) for cur_sum, degree in out]

        return sum([v for v, _ in traverse(root)])
