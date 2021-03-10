#797. All Paths From Source to Target
#Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1, and return them in any order.

#The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ## backtracking
        out= []
        test=1
        def backtrack(graph, path):
            nonlocal out
            if path[-1]==len(graph)-1:
                out.append(list(path)) ## we have to convert list
                return
            cur_idx = path[-1]
            for i in graph[cur_idx]:
                path.append(i)
                backtrack(graph, path)
                path.pop()
        backtrack(graph, [0])
        return out
        
        