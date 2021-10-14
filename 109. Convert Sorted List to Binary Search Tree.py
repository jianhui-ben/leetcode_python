# 109. Convert Sorted List to Binary Search Tree
# Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
#
# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the
# two subtrees of every node never differ by more than 1.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        """
        in order traversal
        O(n) time, O(log n) space
        """
        cnt = 0
        temp = head
        while temp:
            cnt += 1
            temp = temp.next

        temp = head

        def helper(left, right):
            nonlocal
            temp
            if left > right: return None
            mid = (left + right) // 2
            left_res = helper(left, mid - 1)
            root = TreeNode(val=temp.val)
            root.left = left_res
            temp = temp.next
            root.right = helper(mid + 1, right)
            return root

        return helper(0, cnt - 1)

        """
        find the mid index
        root = Node(val = mid)
        root.left = helper(arr, left, mid - 1)
        root.right = helper(arr, mid + 1, right)

        O(n), O(n)
        """
        arr = []
        temp = head
        while temp:
            arr.append(temp.val)
            temp = temp.next

        def helper(left, right):
            if left > right: return None
            mid = (left + right) // 2
            root = TreeNode(val=arr[mid])
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            return root

        return helper(0, len(arr) - 1)



