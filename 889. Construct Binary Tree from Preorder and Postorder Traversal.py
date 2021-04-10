#889. Construct Binary Tree from Preorder and Postorder Traversal
#Return any binary tree that matches the given preorder and postorder traversals.

#Values in the traversals pre and post are distinct positive integers.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        ## space saving version: use index instead of subarray
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:

        def traverse(pre_i, post_i, n):
            if n==0:
                return None
            root = TreeNode(val = pre[pre_i])
            pre_stored, post_stored = defaultdict(int), defaultdict(int)
            for l in range(n):
                pre_stored[pre[pre_i+l+1]]+=1
                post_stored[post[post_i+l]]+=1
                if pre_stored == post_stored:
                    break
            root.left= traverse(pre_i+1, post_i,l+1)
            root.right = traverse(pre_i+l+1, post_i+l, l+1)
            return root
        return traverse(0, 0, len(pre))
        
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        ## O(n**2), spaceO(n)
        if not pre or not post:
            return None
        root=TreeNode(val=pre[0])
        stored_pre, stored_post= defaultdict(int), defaultdict(int)
        temp_pre, temp_post= pre[1:], post[:-1]
        i=-1
        if temp_pre:
            for i in range(len(temp_pre)):
                stored_pre[pre[1+i]]+=1
                stored_post[post[i]]+=1
                if stored_pre==stored_post:
                    break
        
        root.left= self.constructFromPrePost(pre[1: i+2], post[:i+1])
        root.right = self.constructFromPrePost(pre[i+2:], post[i+1:len(post)-1])
        return root


        
        