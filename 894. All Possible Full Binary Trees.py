# 894. All Possible Full Binary Trees
# Given an integer n, return a list of all possible full binary trees with n nodes. Each node of each tree in the answer must have Node.val == 0.
#
# Each element of the answer is the root node of one possible tree. You may return the final list of trees in any order.
#
# A full binary tree is a binary tree where each node has exactly 0 or 2 children.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        """
        divide and concur



        """
        if not n % 2: return []
        if n == 1: return [TreeNode()]

        out = []
        for i in range((n - 1) // 2):
            left = self.allPossibleFBT(i * 2 + 1)
            right = self.allPossibleFBT(n - 1 - (i * 2 + 1))
            for left_node in left:
                for right_node in right:
                    cur_root = TreeNode()
                    cur_root.left = left_node
                    cur_root.right = right_node
                    out.append(cur_root)
        return out


