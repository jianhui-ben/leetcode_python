# 99. Recover Binary Search Tree
# You are given the root of a binary search tree (BST), where the values of exactly two
# nodes of the tree were swapped by mistake. Recover the tree without changing its structure.
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        """
        inorder traversal to find two swapping occurence:
        l[i + 1] < l[i], record l[i + 1] and l[i]
        """
        fir = sec = pre = None

        def helper(node):
            nonlocal fir, sec, pre
            if not node: return

            helper(node.left)

            if pre and node.val < pre.val:

                sec = node
                if not fir:
                    fir = pre
                else:
                    return
            pre = node
            helper(node.right)

        helper(root)
        # print(fir.val, sec.val)
        fir.val, sec.val = sec.val, fir.val
