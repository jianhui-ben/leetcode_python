# 1631. Path With Minimum Effort
# You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.
#
# A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.
#
# Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

import heapq


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        """
        dijkstra BFS
        """
        dp = [[float('inf') for _ in range(len(heights[0]))] for r in range(len(heights))]
        ## min, max
        # dp[0][0] = 0
        ## abs dif, row, col
        queue, dir_ = [(0, 0, 0)], [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            cur_dif, row, col = heapq.heappop(queue)
            if row == len(heights) - 1 and col == len(heights[0]) - 1:
                return cur_dif

            if cur_dif >= dp[row][col]:
                continue
            dp[row][col] = cur_dif

            for d_r, d_c in dir_:
                new_r, new_c = d_r + row, d_c + col
                if 0 <= new_r < len(heights) and 0 <= new_c < len(heights[0]) \
                        and max(cur_dif, abs(heights[new_r][new_c] - heights[row][col])) \
                        < dp[new_r][new_c]:
                    new_dif = max(cur_dif, abs(heights[new_r][new_c] - heights[row][col]))
                    heapq.heappush(queue, (new_dif, new_r, new_c))
        print(dp)






