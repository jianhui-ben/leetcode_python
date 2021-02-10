#1110. Delete Nodes And Return Forest


#Given the root of a binary tree, each node in the tree has a distinct value.

#After deleting all nodes with a value in to_delete, we are left with a forest 
#(a disjoint union of trees).

#Return the roots of the trees in the remaining forest.  You may return the result in any order.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        
        
        ##post-order DFS to find the node, delete
        out=[]
        def delete_node(node):
            if node:
                delete_node(node.left)
                if node.left and node.left.val in to_delete:
                    to_delete.remove(node.left.val)
                    node.left= None
                delete_node(node.right)
                if node.right and node.right.val in to_delete:
                    to_delete.remove(node.right.val)
                    node.right= None
                if node.val in to_delete:
                    if node.left: out.append(node.left)
                    if node.right: out.append(node.right)        

                        
        delete_node(root)
        if root.val not in to_delete:
            out.append(root)
        return out