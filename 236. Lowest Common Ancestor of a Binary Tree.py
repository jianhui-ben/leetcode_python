# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.result = None
        ## find node equal to either p or q, return boolean
        ## time O(n), space O(n)
        def find(root):
            if not root: return False
            l, r = find(root.left), find(root.right)
            mid=root==p or root==q
            if mid+l+r>=2:
                self.result=root
            return mid or l or r

        find(root)
        return self.result
    

        
        
#         ## define a boolean function to recursively search for p or q
#         ## time O(n**2), space O(n2) over time limit
#         def find(root, node):
#             if not root:
#                 return False
#             if root ==node:
#                 return True
#             return find(root.left, node) or find(root.right, node)

        
#         if find(root.left, p) and find(root.left,q):
#             return self.lowestCommonAncestor(root.left, p, q)
        
#         elif find(root.right, p) and find(root.right,q):
#             return self.lowestCommonAncestor(root.right, p, q)
#         else:
#             return root
