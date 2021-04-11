#222. Count Complete Tree Nodes
#Given the root of a complete binary tree, return the number of the nodes in the tree.

#According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        
        ## we can get the depth and the # of nodes in the last level
        ## time O(log n * log n) using binary search
        
        ## we use right->left->left to get the mid index
        ## the last layer can have index 0 to 2**d-1
        ## first get the depth
        if not root: return 0
        d=0
        cur=root
        while cur:
            d+=1
            cur=cur.left
        ## last layer should have 1<= n<= 2**d nodes
        d-=1
        left, right = 1, 2**d  ##1-4， actual 3
        
        def half_is_val(node, temp_d):
            if not node or temp_d<1: return False
            if temp_d==1: return node.right is not None
            node=node.right
            temp_d-=1
            for i in range(temp_d):
                node=node.left
                if not node:
                    return False
            return True
                

        temp_node = root
        temp_d = d
        while left<=right:
            mid = left+ (right-left)//2
            if half_is_val(temp_node, temp_d):
                left= mid+1
                temp_node=temp_node.right
                temp_d-=1
            else:
                right=mid-1
                temp_node=temp_node.left
                temp_d-=1
        ## return left boundary
        return 2**d-1+ left
        
