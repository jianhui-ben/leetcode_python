#366. Find Leaves of Binary Tree
#Given the root of a binary tree, collect a tree's nodes as if you were doing this:

#Collect all the leaf nodes.
#Remove all the leaf nodes.
#Repeat until the tree is empty.
 # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        """
        post-order traversal to get heights for each node
        at every single node, we need to know the max(heights)
        if no children: 
            return 0
        if left:
           return traverse(left) +1
        else: 
        max(leftHeight, rightHeight) + 1
        
        O(N), O(n)
        
        """
        self.stored = defaultdict(list)
        def post_order(node): ## return the max heights of the node
            if not node: return -1
            if not node.left and not node.right:
                self.stored[0].append(node.val)
                return 0
            max_heights = max(post_order(node.left), post_order(node.right))
            self.stored[max_heights + 1].append(node.val)
            
            return max_heights + 1
            

        post_order(root)
        out = []
        for _, nodes in self.stored.items():
            out.append(nodes)

        return out
