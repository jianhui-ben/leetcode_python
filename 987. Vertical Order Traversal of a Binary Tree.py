#987. Vertical Order Traversal of a Binary Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        ## tree traversal and add every node into hashtable
        ## key will be its horizontal axis, value would be (vertical axis and value)
        ## same question as 314
        ## time O(N+WlogW + W*H*log*H); space O(N)
        stored = defaultdict(list)
        
        
        def dfs(node, width, depth):
            if node:
                stored[width].append((depth, node.val))
                dfs(node.left, width-1, depth+1)
                dfs(node.right, width+1, depth+1)

        
        dfs(root, 0, 0)
        
        ## sort the dictionary key and value:
        out=[]
        for key, value in sorted(stored.items()):
            result = sorted(value)
            out.append([i[1] for i in result])
        return out
        
        
        
