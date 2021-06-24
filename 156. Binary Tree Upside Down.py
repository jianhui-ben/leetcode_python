#156. Binary Tree Upside Down
#Given the root of a binary tree, turn the tree upside down and return the new root.

#You can turn a binary tree upside down with the following steps:

#The original left child becomes the new root.
#The original root becomes the new right child.
#The original right child becomes the new left child.


#The mentioned steps are done level by level, it is guaranteed that every node in the given tree has either 0 or 2 children.

 

#Example 1:


#Input: root = [1,2,3,4,5]
#Output: [4,5,2,null,null,3,1]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        ## in order traversal from right to left
        if not root: return None
        if not root.left:
            return root
        
        new_root = self.upsideDownBinaryTree(root.left)
        root.left.left = self.upsideDownBinaryTree(root.right)
        root.left.right = root
        root.left = root.right = None
        
        
        return new_root
        