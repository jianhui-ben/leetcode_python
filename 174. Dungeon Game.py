#174. Dungeon Game
#The demons had captured the princess and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of m x n rooms laid out in a 2D grid. Our valiant knight was initially positioned in the top-left room and must fight his way through dungeon to rescue the princess.

#The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

#Some of the rooms are guarded by demons (represented by negative integers), so the knight loses health upon entering these rooms; other rooms are either empty (represented as 0) or contain magic orbs that increase the knight's health (represented by positive integers).

#To reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

#Return the knight's minimum initial health so that he can rescue the princess.

#Note that any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        ## try bottom up iterative method
        ## status:dp[i][j]= m: at least m lifes from (i, j) to reach to the destination
        ## dp[i][j] = min(dp[i+1][j], dp[i][j+1])-dungeon[i][j] if it>0, else 1
        ## backward traverse
        dp =[[None for _ in range(len(dungeon[0])+1)] for _ in range(len(dungeon)+1)]
        for i in range(len(dp)-1, -1, -1):
            for j in range(len(dp[i])-1, -1, -1):
                if i==len(dungeon) or j==len(dungeon[0]):
                    dp[i][j] = float('inf')
                elif i==len(dungeon)-1 and j==len(dungeon[0])-1:
                    res = 1-dungeon[i][j]
                    dp[i][j]= res if res>0 else 1
                else:
                    res = min(dp[i+1][j], dp[i][j+1])-dungeon[i][j]
                    dp[i][j]= res if res>0 else 1
        return dp[0][0]
        
        
        ## DP
        ## status: x, y
        ## choice: down or right
        ## dp[x][y]= (m, n): at least m life are needed to reach the bottom right form (x, y)
        self.mem=defaultdict()
        def recursion(dungeon, x, y):
            if x==len(dungeon)-1 and y==len(dungeon[0])-1:
                return 1-dungeon[x][y] if dungeon[x][y]<=0 else 1
            if x==len(dungeon) or y==len(dungeon[0]):
                return float('inf')
            if (x,y) in self.mem:
                return self.mem[(x, y)]
            res = min(recursion(dungeon, x+1, y), \
                                   recursion(dungeon, x, y+1))-dungeon[x][y]
            self.mem[(x, y)]= res if res > 0 else 1
            return self.mem[(x, y)]
            
        out = recursion(dungeon, 0, 0)
        return out