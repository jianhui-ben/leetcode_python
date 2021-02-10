#403. Frog Jump
#A frog is crossing a river. The river is divided into some number of units, and at each unit, there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.

#Given a list of stones' positions (in units) in sorted ascending order, determine if the frog can cross the river by landing on the last stone. Initially, the frog is on the first stone and assumes the first jump must be 1 unit.

#If the frog's last jump was k units, its next jump must be either k - 1, k, or k + 1 units. The frog can only jump in the forward direction.

 

#Example 1:

#Input: stones = [0,1,3,5,6,8,12,17]
#Output: true


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        ## dfs with mem
        ## time n**3, space O(n**2)
        return self.dfs(stones, 0, 0, set())
    
    def dfs(self, stones, pos, jump, mem):
        # print(mem)
        if pos==stones[-1]: return True
        if pos not in stones: return False
        if (pos, jump) in mem: return False
        if jump>1 and self.dfs(stones, pos+ jump-1, jump-1, mem):
            return True
        if jump>0 and self.dfs(stones, pos+ jump, jump, mem):
            return True       
        if self.dfs(stones, pos+ jump+1, jump+1, mem):
            return True
        mem.add((pos, jump))
        return False
            
        
        
            
        
        
        
        
    
        
        
        
