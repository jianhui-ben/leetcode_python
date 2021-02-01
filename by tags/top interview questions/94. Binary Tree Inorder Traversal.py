#94. Binary Tree Inorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        import collections
        out=[]
        queue= collections.deque([root])
        
        while queue:
            cur_node= queue.popleft()
            if cur_node: 
                if not cur_node.left and not cur_node.right:
                    out.append(cur_node.val)
                else:
                    if cur_node.right:
                        queue.appendleft(cur_node.right)
                    queue.appendleft(TreeNode(cur_node.val))
                    if cur_node.left:
                        queue.appendleft(cur_node.left)
        return out
