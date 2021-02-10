#934. Shortest Bridge

#In a given 2D binary array A, there are two islands.  (An island is a 4-directionally connected group of 1s not connected to any other 1s.)

#Now, we may change 0s to 1s so as to connect the two islands together to form 1 island.

#Return the smallest number of 0s that must be flipped.  (It is guaranteed that the answer is at least 1.)

 

#Example 1:

#Input: A = [[0,1],[1,0]]
#Output: 1

class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        ##bfs to get the mini number
        ## we use dfs to find all neighbors of the first island

        
        ##find one (x,y) in the first island:
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j]==1:
                    x,y= i, j
                    break
        visited=set()
        queue=[]
        def dfs(x, y):
            if 0<=x<len(A) and 0<=y<len(A[0]) and (x, y) not in visited:
                visited.add((x, y))
                if A[x][y]==1:
                    dfs(x+1,y)
                    dfs(x-1, y)
                    dfs(x,y+1)
                    dfs(x, y-1)
                else:
                    queue.append((x, y, 0))
        
        def available(x, y):
            temp=set()
            for new_x, new_y in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if 0<=new_x<len(A) and 0<=new_y<len(A[0]) and (new_x, new_y) not in visited:
                    temp.add((new_x, new_y))
            return temp

        dfs(x, y)
        while queue:
            # print(queue)
            x, y, step= queue.pop(0)
            for new_x, new_y in available(x, y):
                if A[new_x][new_y]==1:
                    return step+1
                queue.append((new_x, new_y, step+1))
                visited.add((new_x, new_y))
        return None
                
        
        