#739. Daily Temperatures
#Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

#Example 1:

#Input: temperatures = [73,74,75,71,69,72,76,73]
#Output: [1,1,4,2,1,1,0,0]


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        ## O(n) with stack
        
        out=[0]*len(temperatures)
        
        temp=[]
        for i, v in enumerate(temperatures):
            while temp and temp[-1][1]<v:
                prev_i, prev_v = temp.pop()
                out[prev_i] = i-prev_i
            
            temp.append((i, v))
    
        return out