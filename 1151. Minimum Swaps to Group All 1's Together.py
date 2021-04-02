#1151. Minimum Swaps to Group All 1's Together
#Given a binary array data, return the minimum number of swaps required to group all 1’s present in the array together in any place in the array.

#Example 1:

#Input: data = [1,0,1,0,1]
#Output: 1
#Explanation: 
#There are 3 ways to group all 1's together:
#[1,1,1,0,0] using 1 swap.
#[0,1,1,1,0] using 2 swaps.
#[0,0,1,1,1] using 1 swap.
#The minimum is 1.


class Solution:
    def minSwaps(self, data: List[int]) -> int:
        
        ## sliding window
        target= sum(data)
        left, right= 0,0
        out,cum_sum= float('inf'), 0
        while right<len(data):
            cum_sum+=data[right]
            right+=1
            while right-left> target: #cum_sum> target:
                cum_sum-=data[left]
                left+=1
            if right-left==target:
                out=min(out, right-left-cum_sum)
        return out
            