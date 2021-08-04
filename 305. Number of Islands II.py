#305. Number of Islands II
#You are given an empty 2D binary grid grid of size m x n. The grid represents a map where 0's represent water and 1's represent land. Initially, all the cells of grid are water cells (i.e., all the cells are 0's).

#We may perform an add land operation which turns the water at position into a land. You are given an array positions where positions[i] = [ri, ci] is the position (ri, ci) at which we should operate the ith operation.

#Return an array of integers answer where answer[i] is the number of islands after turning the cell (ri, ci) into a land.

#An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

#Example 1:


#Input: m = 3, n = 3, positions = [[0,0],[0,1],[1,2],[2,1]]
#Output: [1,1,2,3]
#Explanation:
#Initially, the 2d grid is filled with water.
#- Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land. We have 1 island.
#- Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land. We still have 1 island.
#- Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land. We have 2 islands.
#- Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land. We have 3 islands.
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        """
        union find
        time: m*n + 4 * K * 2* M * N--> kmn
        space: m*n
        
        to improve we can make each parent cluster similar size, as balanced as possible: k log(m*n)
        
        
        """
        
        def find(cordinates):
            if cordinates not in parents:
                parents[cordinates] = cordinates

            cur_cordinates = cordinates
            while parents[cur_cordinates] != cur_cordinates:
                cur_cordinates = parents[cur_cordinates]
            return cur_cordinates
        
        def union(cordinates, adj_cordinates):
            cordinates_parent, adj_cordinates_parent = find(cordinates),\
                                                       find(adj_cordinates)
            if adj_cordinates_parent == cordinates_parent:
                return adj_cordinates_parent
            if parents_sizes[cordinates_parent] <=parents_sizes[adj_cordinates_parent]:
                parents[cordinates_parent] = adj_cordinates_parent
                parents_sizes[adj_cordinates_parent] +=parents_sizes[cordinates_parent]
            else:
                parents[adj_cordinates_parent] = cordinates_parent
                parents_sizes[cordinates_parent] +=parents_sizes[adj_cordinates_parent]
            
            return adj_cordinates_parent

        
        parents = defaultdict(str)
        parents_sizes = defaultdict(lambda: 1)
        
        out = []
        grid = [[0 for _ in range(n)] for _ in range(m)]
        
        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        size = 0
        for r, c in positions:
            if grid[r][c] == 1:
                out.append(out[-1])
                continue
            grid[r][c] = 1
            size += 1
            original_parents = set()
            for delta_r, delta_c in d:
                adj_r, adj_c = r + delta_r, c + delta_c
                
                if 0 <= adj_r < m and 0 <= adj_c < n and grid[adj_r][adj_c] == 1:
                    original_parent = union(str(r) + '_' + str(c), \
                                            str(adj_r) + '_' + str(adj_c))
                    original_parents.add(original_parent)
                
            size -= len(original_parents)
            
            out.append(size)
        
        return out
                
                    
                    
            
            
        