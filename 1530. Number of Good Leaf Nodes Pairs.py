#1530. Number of Good Leaf Nodes Pairs
#Given the root of a binary tree and an integer distance. A pair of two different leaf nodes of a binary tree is said to be good if the length of the shortest path between them is less than or equal to distance.

#Return the number of good leaf node pairs in the tree.

 

#Example 1:


#Input: root = [1,2,3,null,4], distance = 3
#Output: 1
#Explanation: The leaf nodes of the tree are 3 and 4 and the length of the shortest path between them is 3. This is the only good pair.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        """
        - record all the previsou node in a graph
        - save all the leaf nodes
        - BFS to count how many leaf nodes can current node reach out to
        time: O(N + 1/2 N * distance)--> O(n)
        space: O(N)
        """
        graph = defaultdict(TreeNode)
        leaf_nodes = set()
        
        def dfs(node):
            if not node: return
            if not node.left and not node.right:
                leaf_nodes.add(node)
                return
            if node.left:
                graph[node.left] = node
                dfs(node.left)
            if node.right:
                graph[node.right] = node
                dfs(node.right)
        
        dfs(root)
        
        out = 0
        def bfs(node):
            nonlocal out, distance
            queue = [node]
            visited = set([node])
            cur_dis = 0
            while queue and cur_dis <= distance:
                temp_queue = []
                for node in queue:
                    if node in leaf_nodes:
                        out += 1
                    if node.left and node.left not in visited:
                        temp_queue.append(node.left)
                        visited.add(node.left)
                    if node.right and node.right not in visited:
                        temp_queue.append(node.right)
                        visited.add(node.right)
                    if node in graph and graph[node] not in visited:
                        temp_queue.append(graph[node])
                        visited.add(graph[node])
                queue = temp_queue
                cur_dis += 1
            out -= 1
            return
        
        for leaf in leaf_nodes:
            bfs(leaf)
        
        return out // 2
        