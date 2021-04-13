#1382. Balance a Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        ## time O(n), space O(n)
        ## stored the sorted node value into an arrary
        ## then create a BST from the sorted array using recursion
        
        ## inorder traversal O(n)
        self.arr = []
        def traverse(node):
            if not node: return
            traverse(node.left)
            self.arr.append(node.val)
            traverse(node.right)
        
        traverse(root)
        
        def buildBST(arr):
            if not arr: return None
            mid = len(arr)//2
            
            root_node=TreeNode(val= arr[mid])
            root_node.left= buildBST(arr[:mid])
            root_node.right= buildBST(arr[mid+1:])
            
            return root_node
            
        return buildBST(self.arr)
        