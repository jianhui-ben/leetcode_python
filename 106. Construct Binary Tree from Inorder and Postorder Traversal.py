#106. Construct Binary Tree from Inorder and Postorder Traversal

#Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        
        ##inorder [9,3,15,20,7]
        ## postorder= [9,15,7,20,3]
        
        inorder_store= defaultdict()
        for i, v in enumerate(inorder):
            inorder_store[v]=i
        
        def buildTreeNode(in_start, in_end, post_start, post_end):
            nonlocal inorder, postorder, inorder_store
            if in_start>in_end: return None
            
            root = TreeNode(val = postorder[post_end])
            if in_end>in_start:
                inorder_cut=inorder_store[postorder[post_end]]
                
                postorder_cut = post_start-1
                for i in range(post_end, post_start-1, -1):
                    if inorder_store[postorder[i]]< inorder_store[postorder[post_end]]:
                        postorder_cut=i
                        break
                        
                if postorder_cut>= post_start:
                    root.left = buildTreeNode(in_start, inorder_cut-1, \
                                              post_start, postorder_cut)
                root.right = buildTreeNode(inorder_cut+1, in_end, \
                                          postorder_cut+1, post_end-1)
            return root 
        return buildTreeNode(0, len(inorder)-1, 0, len(postorder)-1)