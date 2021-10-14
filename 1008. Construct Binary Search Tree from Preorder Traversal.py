# 1008. Construct Binary Search Tree from Preorder Traversal
# Given an array of integers preorder, which represents the preorder traversal of a BST (i.e., binary search tree), construct the tree and return its root.
#
# It is guaranteed that there is always possible to find a binary search tree with the given requirements for the given test cases.
#
# A binary search tree is a binary tree where for every node, any descendant of Node.left has a value strictly less than Node.val, and any descendant of Node.right has a value strictly greater than Node.val.
#
# A preorder traversal of a binary tree displays the value of the node first, then traverses Node.left, then traverses Node.right.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        """
        approach 2: O(n) time
        """

        def helper(arr, lower, upper):
            nonlocal
            idx
            if idx == len(arr):
                return None
            val = arr[idx]
            if val <= lower or val >= upper:
                return None
            root = TreeNode(val=val)
            idx += 1
            root.left = helper(arr, lower, val)
            root.right = helper(arr, val, upper)
            return root

        idx = 0
        return helper(preorder, float('-inf'), float('inf'))

        """
        approach 1: NlogN
        [8,5,1,7,10,12]
        root = Node(8)

        root.left = bst([5, 1, 7])
        root.right = bst([10, 12])
        use binary search
        """

        def first_larger(l, left, right, target):
            ## binary search, return left boundary
            while left <= right:
                mid = left + (right - left) // 2
                if l[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        def bst(l, start, end):
            if start > end: return None
            if start == end:
                return TreeNode(val=l[start])

            ## need to find the first index i where l[i] > l[start]
            root = TreeNode(val=l[start])
            i = first_larger(l, start + 1, end, l[start])
            if i == start + 1:
                root.right = bst(l, start + 1, end)
            else:
                root.left = bst(l, start + 1, i - 1)
                root.right = bst(l, i, end)
            return root

        return bst(preorder, 0, len(preorder) - 1)



