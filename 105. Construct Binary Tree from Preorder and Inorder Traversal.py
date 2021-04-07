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


##multiple methods:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        ## improved version
        ## we can just store the map before
        stored_pos_inorder, stored_pos_preorder=  defaultdict(), defaultdict()
        for i, v in enumerate(inorder):
            stored_pos_inorder[v]=i
        for i, v in enumerate(preorder):
            stored_pos_preorder[v]=i
            
        def buildTreeNode(pre_start_i, pre_end_i, in_start_i, in_end_i):
            ##debug
            # print(pre_start_i, pre_end_i, in_start_i, in_end_i)
            nonlocal stored_pos_inorder, preorder, inorder
            if pre_end_i< pre_start_i:
                return None
            root = TreeNode(val = preorder[pre_start_i])
            if pre_end_i>pre_start_i:
                pos_head_inorder= stored_pos_inorder[preorder[pre_start_i]]
                ## inorder[:pos_head_inorder] and inorder[pos_head_inorder+1:]

                ## for preorder, we need to find the index of right node in preorder
                right_node_i=pre_end_i+1
                for i in range(pre_start_i+1, pre_end_i+1):
                    if stored_pos_inorder[preorder[i]]>\
                    stored_pos_inorder[preorder[pre_start_i]]:
                        right_node_i= i
                        break
                root.left = buildTreeNode(pre_start_i+1, right_node_i-1, in_start_i, pos_head_inorder-1)
                if right_node_i<=pre_end_i:
                    root.right = buildTreeNode(right_node_i, pre_end_i, pos_head_inorder+1, in_end_i)
            return root
            
        return buildTreeNode(0, len(preorder)-1, 0, len(inorder)-1)
        
        
        
        
        
        
        
        ## time O(n**2), space O(n**2)
        if not preorder: return None
        
        root = TreeNode(val=preorder[0])
        if len(preorder)>1:
            i_inorder = inorder.index(preorder[0])
            ## we also need to find the value in the left and right child
            stored_pos_inorder =  defaultdict()
            for i, v in enumerate(inorder):
                stored_pos_inorder[v]=i
            right_i_pre=None
            for i, v in enumerate(preorder):
                if stored_pos_inorder[v]>stored_pos_inorder[preorder[0]]:
                    ## we find the right node on preorder list
                    right_i_pre= i
                    break
            # print(i_inorder,right_i_pre) 
            root.left = self.buildTree(preorder[1:right_i_pre], inorder[:i_inorder])
            if right_i_pre:
                root.right = self.buildTree(preorder[right_i_pre:], inorder[i_inorder+1:])
        
        return root

    
    
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
