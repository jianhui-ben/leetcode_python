#1632. Rank Transform of a Matrix
#Given an m x n matrix, return a new matrix answer where answer[row][col] is the rank of matrix[row][col].

#The rank is an integer that represents how large an element is compared to other elements. It is calculated using the following rules:

#The rank is an integer starting from 1.
#If two elements p and q are in the same row or column, then:
#If p < q then rank(p) < rank(q)
#If p == q then rank(p) == rank(q)
#If p > q then rank(p) > rank(q)
#The rank should be as small as possible.
#It is guaranteed that answer is unique under the given rules.

 

#Example 1:


#Input: matrix = [[1,2],[3,4]]
#Output: [[1,2],[2,3]]
#Explanation:
#The rank of matrix[0][0] is 1 because it is the smallest integer in its row and column.
#The rank of matrix[0][1] is 2 because matrix[0][1] > matrix[0][0] and matrix[0][0] is rank 1.
#The rank of matrix[1][0] is 2 because matrix[1][0] > matrix[0][0] and matrix[0][0] is rank 1.
#The rank of matrix[1][1] is 3 because matrix[1][1] > matrix[0][1], matrix[1][1] > matrix[1][0], and both matrix[0][1] and matrix[1][0] are rank 2.


class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        sort the matrix values and store their values and coordinates
        go from the coordinates with small values, update the rowRank and colRank
        the rank of the current coordinates should be max(rowRank, colRank)
        same values will have the same rank with union find method
        """
        ## store the graph
        graphs = {}
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                val = matrix[row][col] 
                if val not in graphs:
                    graphs[val] = defaultdict(list)
                graphs[val][row].append(~col)
                graphs[val][~col].append(row)

        ## perform BFS to get connected points
        
        connected_points = defaultdict(list)
        visited = set()
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if (row, col) in visited:
                    continue
                val = matrix[row][col]
                visited.add((row, col))
                graph = graphs[val]
                q = [row, ~col]
                rowcols = set([row, ~col])
                while q:
                    cur_rowcol = q.pop(0)
                    for next_rowcol in graph[cur_rowcol]:
                        if next_rowcol not in rowcols:
                            q.append(next_rowcol)
                            rowcols.add(next_rowcol)
                
                points = set()
                for rowcol in rowcols:
                    for k in graph[rowcol]:
                        if k >= 0:
                            point = (k, ~rowcol)
                        else:
                            point = (rowcol, ~k)

                        points.add(point)
                        visited.add(point)
                connected_points[val].append(points)
        
            
        
        out = [[None for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        rowRank, colRank = defaultdict(int), defaultdict(int)
        # print(connected_points)
        connected_points = sorted(connected_points.items())
        
        for _, group_points in connected_points:
            for points in group_points:
                
                rank = -1
                
                for row, col in points:
                    rank = max(rank, max(rowRank[row], colRank[col]) + 1)
                for row, col in points:
                    out[row][col] = rank
                    rowRank[row] = max(rowRank[row], rank)
                    colRank[col] = max(colRank[col], rank)
                    
        return out
        
                    
            

                    
                    
                                       