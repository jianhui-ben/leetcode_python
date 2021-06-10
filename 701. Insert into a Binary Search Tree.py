#701. Insert into a Binary Search Tree

#You are given the root node of a binary search tree (BST) and a 
#value to insert into the tree. Return the root node of the BST after the 
#insertion. It is guaranteed that the new value does not exist in the original BST.

#Notice that there may exist multiple valid ways for the insertion, as long as 
#the tree remains a BST after insertion. You can return any of them.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        
        ## recursive approach
        if not root:
            return TreeNode(val=val)
        if val<root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root


        ##iterative approach 
        node, temp= root, None
        while node:
            temp=node
            if val>node.val:
                node=node.right
            else:
                node=node.left
        
        if not temp:
            return TreeNode(val=val)
        elif val> temp.val:
            temp.right = TreeNode(val=val)
        elif val< temp.val:
            temp.left = TreeNode(val=val)
        return root
            
        
            