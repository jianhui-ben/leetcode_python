#1197. Minimum Knight Moves

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        
        ## definitely check this A* search
            x, y = abs(x), abs(y)
            moves = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (2, -1)]

            def heuristic(x1, y1):
                return sqrt((x-x1)**2 + (y-y1)**2)

            pq = [(0, 0, (0, 0))]

            while pq: 
                h, steps, prev = heappop(pq)
                if prev == (x, y): 
                    return steps
                for move in moves: 
                    dest = (prev[0] + move[0], prev[1] + move[1])
                    heappush(pq, (steps + 1 + heuristic(dest[0], dest[1]), steps + 1, dest))
# class Solution:
#     def minKnightMoves(self, x: int, y: int) -> int:
#         ## BFS:
#         step=0
#         queue = [(0,0)]
#         visited=set([(0, 0)])
#         actual_distance = x**2+y**2+5
#         def next_pos(pos, visited, x, y):
#             nonlocal actual_distance
#             a,b = pos
#             temp=[]
#             for m, n in [(1,2), (1, -2), (-1, 2), (-1, -2),\
#                         (2,1), (-2, 1), (2, -1), (-2, -1)]:
#                 new_a, new_b = a+m, b+n
#                 if new_a>=0 and (new_a, new_b) not in visited:
#                     temp.append((new_a, new_b))
#                     visited.add((new_a, new_b))
#             return temp

#         x, y= abs(x), abs(y)
#         while queue:
#             temp=[]
#             for pos in queue:
#                 if pos == (x, y):
#                     return step
#                 temp=temp+next_pos(pos, visited, x, y)
#             queue=temp
#             step+=1
#         return None
            
