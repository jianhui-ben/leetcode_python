# 662. Maximum Width of Binary Tree
# Given the root of a binary tree, return the maximum width of the given tree.
#
# The maximum width of a tree is the maximum width among all levels.
#
# The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes are also counted into the length calculation.
#
# It is guaranteed that the answer will in the range of 32-bit signed integer.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        BFS
        time: O(n), space O(n)
        """
        out, queue = 1, [(root, 0)]
        while queue:
            temp = []
            cur_min, cur_max = float('inf'), float('-inf')
            for node, i in queue:
                if node.left:
                    temp.append((node.left, i * 2))
                    cur_min = min(cur_min, i * 2)
                    cur_max = max(cur_max, i * 2)
                if node.right:
                    temp.append((node.right, i * 2 + 1))
                    cur_min = min(cur_min, i * 2 + 1)
                    cur_max = max(cur_max, i * 2 + 1)
            out = max(out, cur_max - cur_min + 1)
            queue = temp
        return out

#         """
#         index of same level nodes in binary tree
#         a parent node with index i in level L1 will have left child with 2 * i in L1 + 1 and 2 * i + 1 in L1 + 1

#         helper(left_node, right_node,  left_i, right_i)
#         time: 4 ** N
#         """
#         out = 1
#         def helper(left_node, right_node, left_i, right_i):
#             nonlocal out
#             if not left_node and not right_node: return
#             elif not left_node: helper(right_node, right_node, right_i, right_i)
#             elif not right_node: helper(left_node, left_node, left_i, left_i)
#             else:
#                 out = max(out, right_i - left_i + 1)
#                 helper(left_node.left, right_node.left, left_i * 2, right_i * 2)
#                 helper(left_node.left, right_node.right, left_i * 2, right_i * 2 + 1)
#                 helper(left_node.right, right_node.left, left_i * 2 + 1, right_i * 2)
#                 helper(left_node.right, right_node.right, left_i * 2 + 1, right_i * 2 + 1)

#         helper(root, root, 0, 0)
#         return out