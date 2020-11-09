#133. Clone Graph
#Given a reference of a node in a connected undirected graph.

#Return a deep copy (clone) of the graph.

#Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

#class Node {
#    public int val;
#    public List<Node> neighbors;
#}

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

##BFS with a queue and a hashtable to store edges
## time O(# of nodes + # of edges) space O(n= # of nodes in the graph)
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        queue=[]
        queue.append(node)
        table= dict()
        copy_start= Node(val=node.val)
        table[node]=copy_start
        while queue:
            cur_node= queue.pop(0)
            for neigh in cur_node.neighbors:
                if neigh not in table:
                    copy_neigh= Node(val=neigh.val)
                    table[neigh]= copy_neigh
                    queue.append(neigh)
                    table[cur_node].neighbors.append(copy_neigh)
                else:
                    table[cur_node].neighbors.append(table[neigh])
        return copy_start