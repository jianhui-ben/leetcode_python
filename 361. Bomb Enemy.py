#361. Bomb Enemy
#Given an m x n matrix grid where each cell is either a wall 'W', an enemy 'E' or empty '0', return the maximum enemies you can kill using one bomb. You can only place the bomb in an empty cell.

#The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since it is too strong to be destroyed.

 

#Example 1:


#Input: grid = [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]
#Output: 3
class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        """
        Brute force:
        O(M*N) *(M+N), O(1)
        
        
        
        only consider to right
        1  X 0 0
        X  0 X X
        1  X 0 0
        
        to left
        0  X 1 1
        X  1 X X
        0  X 1 1
        
        up:
        0  X 0 0  
        X  1 X X
        1  X X 1
        
        if E: cur_cnt += 1
        if W: cur_cnt = 0
        if '0': enter cur_cnt
        O(NM), O(NM)
        """
        result = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        ## boom to left:
        for i in range(len(grid)):
            cur_cnt = 0
            for j in range(len(grid[0])):
                if grid[i][j] == 'E':
                    cur_cnt += 1
                elif grid[i][j] == 'W':
                    cur_cnt = 0
                else:
                    result[i][j] += cur_cnt
        
        ## boom to right:
        for i in range(len(grid)):
            cur_cnt = 0
            for j in range(len(grid[0])-1, -1, -1):
                if grid[i][j] == 'E':
                    cur_cnt += 1
                elif grid[i][j] == 'W':
                    cur_cnt = 0
                else:
                    result[i][j] += cur_cnt
                    
        ## boom downwards:
        for j in range(len(grid[0])):
            cur_cnt = 0
            for i in range(len(grid)):
                if grid[i][j] == 'E':
                    cur_cnt += 1
                elif grid[i][j] == 'W':
                    cur_cnt = 0
                else:
                    result[i][j] += cur_cnt

        ## boom upwards:
        for j in range(len(grid[0])):
            cur_cnt = 0
            for i in range(len(grid)-1, -1, -1):
                if grid[i][j] == 'E':
                    cur_cnt += 1
                elif grid[i][j] == 'W':
                    cur_cnt = 0
                else:
                    result[i][j] += cur_cnt
        return max([max(row) for row in result])
        
        
        
        
        
        
        
        
        
        
        
        