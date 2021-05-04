#174. Dungeon Game
#The demons had captured the princess and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of m x n rooms laid out in a 2D grid. Our valiant knight was initially positioned in the top-left room and must fight his way through dungeon to rescue the princess.

#The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

#Some of the rooms are guarded by demons (represented by negative integers), so the knight loses health upon entering these rooms; other rooms are either empty (represented as 0) or contain magic orbs that increase the knight's health (represented by positive integers).

#To reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

#Return the knight's minimum initial health so that he can rescue the princess.

#Note that any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.

 
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
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