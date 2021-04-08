#173. Binary Search Tree Iterator
#Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

#BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
#boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
#int next() Moves the pointer to the right, then returns the number at the pointer.
#Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.

#You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator:
    ## approach one: flatten the BST into an inorder array
    ## it's bad in space, since it stored the whole array

    def __init__(self, root: TreeNode):
        ## time O(n), space O(n)
        
        self.in_order_stack=[]
        def traverse(node):
            if node:
                traverse(node.left)
                self.in_order_stack.append(node)
                traverse(node.right)
        traverse(root)
        self.cur_i= -1

    def next(self) -> int:
        self.cur_i+=1
        return self.in_order_stack[self.cur_i].val

    def hasNext(self) -> bool:
        return self.cur_i<len(self.in_order_stack)-1
        
        
        
class BSTIterator:
    ## approach 2: if the max space complexity is O(H)
    def __init__(self, root: TreeNode):
        ## time O(h), space O(h)
        self.root = root
        self.stack=[]
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        ##time O(h)
        cur_node = self.stack.pop()
        temp=cur_node.right
        while temp:
            self.stack.append(temp)
            temp=temp.left
        return cur_node.val

    def hasNext(self) -> bool:
        return len(self.stack)>0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
