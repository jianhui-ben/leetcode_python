#679. 24 Game

#You have 4 cards each containing a number from 1 to 9. You need to judge whether they could operated through *, /, +, -, (, ) to get the value of 24.

#Example 1:
#Input: [4, 1, 8, 7]
#Output: True
#Explanation: (8-4) * (7-1) = 24

class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        return self.dfs([float(i) for i in nums])
    
    
    def dfs(self, l):
        if len(l)==1 and abs(l[0]-24)<2e-10: return True
        for i1 in range(len(l)):
            for i2 in range(len(l)):
                if i1==i2: continue
                
                a, b= l[i1], l[i2]
                rest= [val for idx, val in enumerate(l) if idx!=i1 and idx!=i2]
                
                if self.dfs(rest+[a+b]): return True
                if self.dfs(rest+[a-b]): return True
                if self.dfs(rest+[a*b]): return True
                if b!=0:
                    if self.dfs(rest+[a/b]): 
                        return True
        return False  
            
                
        
        
        
        