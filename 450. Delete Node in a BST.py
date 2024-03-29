#450. Delete Node in a BST

#Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

#Basically, the deletion can be divided into two stages:

#Search for a node to remove.
#If the node is found, delete the node.
#Follow up: Can you solve it with time complexity O(height of tree)?

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        #O(log n), O(log n)
        
        if not root: return None
        if root.val==key:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            ## we find the smallest of the root.right to become the new_root
            new_val = self.getMin(root.right)
            root.val = new_val
            root.right = self.deleteNode(root.right, new_val)
            return root
        elif root.val> key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
            
        return root
    
    def getMin(self, node):
        while node.left:
            node = node.left
        return node.val