#286. Walls and Gates
#You are given an m x n grid rooms initialized with these three possible values.

#-1 A wall or an obstacle.
#0 A gate.
#INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
#Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        ## bfs:
        queue= []
        for r in range(len(rooms)):
            for c in range(len(rooms[0])):
                if rooms[r][c]==0:
                    queue.append((r,c, 0)) 
                    
        while queue:
            r,c, l= queue.pop(0)
            for new_r, new_c in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if new_r>=0 and new_c>=0 and new_r<len(rooms) and \
                new_c<len(rooms[0]) and rooms[new_r][new_c]==2**31 -1:
                    rooms[new_r][new_c]=l+1
                    queue.append((new_r, new_c, l+1))
        return rooms
                    
                    
        
        
        
        
        
        
        
#         ## dfs: relatively slow
#         def dfs(rooms, r,c, l, visited):
#             if r>=0 and c>=0 and r<len(rooms) and c<len(rooms[0]) and rooms[r][c]>0\
#             and (r, c) not in visited:
#                 rooms[r][c]= min(rooms[r][c], l)
#                 dfs(rooms, r+1, c, l+1, visited+[(r, c)])
#                 dfs(rooms, r-1, c, l+1, visited+[(r, c)])
#                 dfs(rooms, r, c+1, l+1, visited+[(r, c)])
#                 dfs(rooms, r, c-1, l+1, visited+[(r, c)])

#         for r in range(len(rooms)):
#             for c in range(len(rooms[0])):
#                 if rooms[r][c]==0:
#                     dfs(rooms, r+1, c, 1, [(r, c)])
#                     dfs(rooms, r-1, c, 1, [(r, c)])
#                     dfs(rooms, r, c+1, 1, [(r, c)])
#                     dfs(rooms, r, c-1, 1, [(r, c)])
#         return rooms
                
        