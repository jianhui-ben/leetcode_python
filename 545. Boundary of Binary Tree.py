#545. Boundary of Binary Tree
#The boundary of a binary tree is the concatenation of the root, the left boundary, the leaves ordered from left-to-right, and the reverse order of the right boundary.

#The left boundary is the set of nodes defined by the following:

#The root node's left child is in the left boundary. If the root does not have a left child, then the left boundary is empty.
#If a node in the left boundary and has a left child, then the left child is in the left boundary.
#If a node is in the left boundary, has no left child, but has a right child, then the right child is in the left boundary.
#The leftmost leaf is not in the left boundary.
#The right boundary is similar to the left boundary, except it is the right side of the root's right subtree. Again, the leaf is not part of the right boundary, and the right boundary is empty if the root does not have a right child.

#The leaves are nodes that do not have any children. For this problem, the root is not a leaf.

#Given the root of a binary tree, return the values of its boundary.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        
        ## brute force
        self.out=[]
        
        def leftBound(root):
            ##pre-order
            if not root.right and not root.left: return
            
            self.out.append(root.val)
            if not root.left: leftBound(root.right)
            else: leftBound(root.left)
            
        def getLeaf(root):
            if root:
                if not root.right and not root.left: 
                    self.out.append(root.val)
                if root.left:
                    getLeaf(root.left)
                if root.right:
                    getLeaf(root.right)
                    
        def rightBound(root):
            ## post order
            if not root.right and not root.left: return
            if not root.right: rightBound(root.left)
            else: rightBound(root.right)
            self.out.append(root.val)
            
            
        
        self.out.append(root.val)
        if root and root.left:
            leftBound(root.left)
            print(self.out)
            
        if root and (root.left or root.right):
            getLeaf(root)
        print(self.out)
        if root and root.right:
            rightBound(root.right)
            print(self.out)
        
        return self.out
        
