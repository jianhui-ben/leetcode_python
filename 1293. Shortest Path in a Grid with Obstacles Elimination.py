#1293. Shortest Path in a Grid with Obstacles Elimination
#Given a m * n grid, where each cell is either 0 (empty) or 1 (obstacle). In one step, you can move up, down, left or right from and to an empty cell.

#Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m-1, n-1) given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.

 

#Example 1:

#Input: 
#grid = 
#[[0,0,0],
# [1,1,0],
# [0,0,0],
# [0,1,1],
# [0,0,0]], 
#k = 1
#Output: 6
#Explanation: 
#The shortest path without eliminating any obstacle is 10. 
#The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        ### standard bfs
        
        mem=set(['0_0_0']) ## save x,y, # o obstacles
        
        def available(grid, x, y, obs):
            temp=set()
            for new_x, new_y in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if 0<=new_x<len(grid) and 0<=new_y<len(grid[0]):
                    if obs+grid[new_x][new_y]<=k and \
                    '_'.join([str(new_x), str(new_y), \
                              str(obs+grid[new_x][new_y])]) not in mem:
                        temp.add((new_x, new_y, obs+grid[new_x][new_y]))
            return temp
        
        def bfs(grid, queue):
            while queue:
                # print(queue)
                x, y, step, obs=queue.pop(0)
                if x==len(grid)-1 and y==len(grid[0])-1 and obs<=k:
                    return step
                for new_x, new_y, new_obs in available(grid, x, y, obs):
                    queue.append((new_x, new_y, step+1, new_obs))
                    mem.add('_'.join([str(new_x), str(new_y), str(new_obs)]))
            return -1
        return bfs(grid, [(0, 0, 0, 0)])
    