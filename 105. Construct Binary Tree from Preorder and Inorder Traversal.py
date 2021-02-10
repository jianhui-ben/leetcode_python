#105. Construct Binary Tree from Preorder and Inorder Traversal

#Given preorder and inorder traversal of a tree, construct the binary tree.

#Note:
#You may assume that duplicates do not exist in the tree.

#For example, given

#preorder = [3,9,20,15,7]
#inorder = [9,3,15,20,7]
#Return the following binary tree:

#    3
#   / \
#  9  20
#    /  \
#   15   7


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def helper(self, prestart, instart, inend, preorder, inorder):
#         if prestart>len(preorder)-1 or instart>inend: return None 
        
#         root=TreeNode(val=preorder[prestart])
        
#         inindex=0
#         for i in range(instart, inend):
#             if inorder[i]==root.val:
#                 inindex=i
        
#         root.left= self.helper(prestart+1, instart, inindex-1, preorder, inorder)
#         root.right=self.helper(prestart+inindex-instart+1, inindex+1,inend, preorder, inorder)

#         return root
    
    
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
#         return self.helper(0, 0, len(inorder)-1, preorder, inorder)
    
    
    
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        hm={}
        for i,val in enumerate(inorder):
            hm[val]=i
        def build(prestart,preend,instart,inend):
            if prestart > preend:
                return None
            val=preorder[prestart]
            index=hm[val]
            leftlen=index-instart
            rightlen=inend-index
            root = TreeNode(val)
            root.left=build(prestart+1,prestart+leftlen,instart,index-1)
            root.right=build(prestart+leftlen+1,prestart+leftlen+rightlen,index+1,inend)
            return root
        return build(0,len(preorder)-1,0,len(inorder)-1)
