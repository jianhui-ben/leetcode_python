# 129. Sum Root to Leaf Numbers
# You are given the root of a binary tree containing digits from 0 to 9 only.
#
# Each root-to-leaf path in the tree represents a number.
#
# For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
# Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.
#
# A leaf node is a node with no children.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        """
        store all root to leaf path into a list of lsts

        dfs([], root)
        if not node: append cur_path
        backtracking
        time: O(n), space O(h)
        """
        ans = 0

        def dfs(node, cur_path):
            nonlocal ans
            if not node.left and not node.right:
                ans += int(''.join(cur_path[:]))
                return

            if node.left:
                dfs(node.left, cur_path + [str(node.left.val)])
            if node.right:
                dfs(node.right, cur_path + [str(node.right.val)])

        if not root: return 0
        dfs(root, [str(root.val)])
        return ans
