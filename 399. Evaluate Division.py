# 399. Evaluate Division
# You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.
#
# You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.
#
# Return the answers to all queries. If a single answer cannot be determined, return -1.0.
#
# Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.
#
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        use union find to determine if Ai and Bi have the answer (have the same parents)
        build a graph and then find the shortest path from Ai to Bi
        """
        graph, variables = defaultdict(list), set()
        for i, equation in enumerate(equations):
            variables.add(equation[0])
            variables.add(equation[1])
        uf = {i: i for i in variables}

        def find(a):
            nonlocal uf
            while uf[a] != a:
                uf[a] = uf[uf[a]]
                a = uf[a]
            return a

        def union(a, b):
            nonlocal uf
            a_root, b_root = find(a), find(b)
            if a_root == b_root: return
            uf[a_root] = b_root
            return

        for i, equation in enumerate(equations):
            a, b = equation[0], equation[1]
            union(a, b)
            graph[a].append((b, values[i]))
            graph[b].append((a, 1 / values[i]))

        out = [None] * len(queries)

        def distance_ratio(graph, c, d):
            queue, visited = [(c, 1)], set([c])
            while queue:
                temp = []
                for variable, ratio in queue:
                    for next_v, next_r in graph[variable]:
                        if next_v == d:
                            return ratio * next_r

                        if next_v not in visited:
                            temp.append((next_v, ratio * next_r))
                            visited.add(next_v)
                queue = temp
            return

        for i, query in enumerate(queries):
            c, d = query[0], query[1]
            # print(find(uf, c), find(uf, d))

            if c not in variables or d not in variables or find(c) != find(d):
                out[i] = -1.0
            else:
                out[i] = distance_ratio(graph, c, d)

        return out







