#776. Split BST
#Given the root of a binary search tree (BST) and an integer target, split the tree into two subtrees where one subtree has nodes that are all smaller or equal to the target value, while the other subtree has all nodes that are greater than the target value. It Is not necessarily the case that the tree contains a node with the value target.

#Additionally, most of the structure of the original tree should remain. Formally, for any child c with parent p in the original tree, if they are both in the same subtree after the split, then node c should still have the parent p.

#Return an array of the two roots of the two subtrees.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def splitBST(self, root: TreeNode, target: int) -> List[TreeNode]:
        """
        Returning:
        [left, right]

        if target >= cur_node.val: split should happen on the right
        else: split should happen on the left


        assuming split on the left:

        [left_part, right_part] = split(curnode.left)
        curnode.left = right_part
        return [left_part, curNode]


        assuming split on the right:

        [left_part, right_part] = split(curode.right)
        cur_node.right = left_part
        return [cur_node, right_part]


        split(root)

        time: O(H) --> O(log n)
        space: O(H) --> O(log n)

        """
        if root.val <= target and not root.right:
            return [root, None]
        
        if root.val > target and not root.left:
            return [None, root]
        
        if root.val <= target:
            smaller, larger = self.splitBST(root.right, target)
            root.right = smaller
            return [root, larger]
        
        elif root.val > target:
            smaller, larger = self.splitBST(root.left, target)
            root.left = larger
            return [smaller, root]
        
            
        
        


  
  
