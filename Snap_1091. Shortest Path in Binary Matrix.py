#1091. Shortest Path in Binary Matrix
#In an N by N square grid, each cell is either empty (0) or blocked (1).

#A clear path from top-left to bottom-right has length k if and only if it is composed of cells C_1, C_2, ..., C_k such that:

#Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they are different and share an edge or corner)
#C_1 is at location (0, 0) (ie. has value grid[0][0])
#C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
#If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).
#Return the length of the shortest such clear path from top-left to bottom-right.  If such a path does not exist, return -1.

 class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ## breadth-first search
        if grid[0][0]==1: return -1
        stored={}
        stack=[(0, 0)]
        
        self.bfs(stack, 1, stored, grid)
        print(stored)
        if (len(grid)-1, len(grid[0])-1) in stored:
            return stored[len(grid)-1, len(grid[0])-1]
        else: return -1
    
    def bfs(self, stack, dis, stored, grid):
        if not stack: return
        temp=[]
        hidth, width = len(grid), len(grid[0])
        for (cur_r, cur_c) in stack:
            if (cur_r, cur_c) not in stored:
                stored[cur_r, cur_c]= dis
                if cur_r+1<hidth and grid[cur_r+1][cur_c]==0:
                    temp.append((cur_r+1, cur_c))
                if cur_c+1<width and grid[cur_r][cur_c+1]==0:
                    temp.append((cur_r, cur_c+1))
                if cur_c+1<width and cur_r+1<hidth and grid[cur_r+1][cur_c+1]==0:
                    temp.append((cur_r+1, cur_c+1))
                if cur_c-1>=0 and cur_r+1<hidth and grid[cur_r+1][cur_c-1]==0:
                    temp.append((cur_r+1, cur_c-1))
                if cur_r-1>=0 and cur_c+1<width and grid[cur_r-1][cur_c+1]==0:
                    temp.append((cur_r-1, cur_c+1))
        self.bfs(temp, dis+1, stored, grid)

        