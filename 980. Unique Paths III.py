# 980. Unique Paths III
# You are given an m x n integer array grid where grid[i][j] could be:
#
# 1 representing the starting square. There is exactly one starting square.
# 2 representing the ending square. There is exactly one ending square.
# 0 representing empty squares we can walk over.
# -1 representing obstacles that we cannot walk over.
# Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        """
        backtrack(current_position, current_grid, empty_cnt)
        """
        self.out, empty = 0, 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    start = (r, c)
                elif grid[r][c] == 2:
                    self.target = (r, c)
                elif grid[r][c] == 0:
                    empty += 1

        def backtrack(cur_r, cur_c, grid, empty, visited):
            if (cur_r, cur_c) == self.target and empty == -1:
                self.out += 1
                return
            elif (cur_r, cur_c) == self.target:
                return

            for d_r, d_c in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_r, new_c = d_r + cur_r, d_c + cur_c
                if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]) and grid[new_r][new_c] != -1 \
                        and (new_r, new_c) not in visited:
                    temp = grid[new_r][new_c]
                    grid[new_r][new_c] = 2
                    visited.add((new_r, new_c))
                    backtrack(new_r, new_c, grid, empty - 1, visited)
                    grid[new_r][new_c] = temp
                    visited.remove((new_r, new_c))

        backtrack(start[0], start[1], grid, empty, set([start]))
        return self.out



