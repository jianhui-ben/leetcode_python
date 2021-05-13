#337. House Robber III
#The thief has found himself a new place for his thievery again. There is only one entrance to this area, called root.

#Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that all houses in this place form a binary tree. It will automatically contact the police if two directly-linked houses were broken into on the same night.

#Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        ## status: current position, pick this or not
        ## dp[root][1]=dp[root.left][0]+dp[root.right][0]
        ## dp[root][0]=max(dp[root.left][0],dp[root.left][1]) + \
        ##             max(dp[root.right][0],dp[root.right][1])
        def dp(node):
            if not node:
                return [0, 0]
            right_, left_ = dp(node.left), dp(node.right)
            rob_node =  right_[0]+left_[0]+ node.val
            not_rob_node = max(right_)+max(left_)
            return [not_rob_node, rob_node]
        out = dp(root)
        return max(out)
        
        
        
        

        
        ## approach 2: mem
        self.mem = defaultdict()
        
        def rob_node(node):
            if not node:
                return 0
            if node in self.mem:
                return self.mem[node]
            rob_this = node.val
            if node.left:
                rob_this+=rob_node(node.left.left)+rob_node(node.left.right)
            if node.right:
                rob_this+=rob_node(node.right.left)+rob_node(node.right.right)                
            self.mem[node] = max(rob_this, rob_node(node.left)+ rob_node(node.right))
            return self.mem[node]
        return rob_node(root)