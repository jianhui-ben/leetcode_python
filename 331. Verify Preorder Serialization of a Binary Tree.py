#331. Verify Preorder Serialization of a Binary Tree
#One way to serialize a binary tree is to use preorder traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as '#'.


#For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where '#' represents a null node.

#Given a string of comma-separated values preorder, return true if it is a correct preorder traversal serialization of a binary tree.

#It is guaranteed that each comma-separated value in the string must be either an integer or a character '#' representing null pointer.

#You may assume that the input format is always valid.

#For example, it could never contain two consecutive commas, such as "1,,3".
#Note: You are not allowed to reconstruct the tree.

 

#Example 1:

#Input: preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
#Output: true


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        """
        approach 2: constant space to track the slots
        
        """
        i, slot = 0, 1
        while i < len(preorder):
            i_start = i
            while i < len(preorder) and preorder[i] != ',':
                i += 1
            slot -= 1
            if slot < 0: 
                return False
            if preorder[i_start : i] != '#':
                slot += 2
            i += 1
        
        return slot == 0
                

        
#         """
#         approach 1
#         stack
#         """
#         stack = []
#         for node in preorder.split(','):
#             stack.append(node)
#             while len(stack) >= 3 and stack[-1] == '#' and stack[-2] == '#' and stack[-3] != '#':
#                 stack.pop()
#                 stack.pop()
#                 stack[-1] = '#'

#         return stack == ['#']