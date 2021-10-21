# 250. Count Univalue Subtrees
# Given the root of a binary tree, return the number of uni-value subtrees.
#
# A uni-value subtree means all nodes of the subtree have the same value.
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        """
        postorder traversal

        helper(node) return inf if the subtree are not the same value, else return uni-val

        """
        self.ans = 0

        def traverse(node):
            if not node: return float('inf')

            uni_val_left, uni_val_right = traverse(node.left), traverse(node.right)
            if uni_val_left == uni_val_right == float('inf'):
                self.ans += 1
                return node.val
            elif (uni_val_left == float('inf') and uni_val_right == node.val) \
                    or (uni_val_right == float('inf') and uni_val_left == node.val):
                self.ans += 1
                return node.val
            elif uni_val_left == uni_val_right == node.val:
                self.ans += 1
                return node.val
            return float('-inf')

        traverse(root)

        return self.ans

