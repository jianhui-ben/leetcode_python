#1262. Greatest Sum Divisible by Three
#Given an array nums of integers, we need to find the maximum possible sum of elements of the array such that it is divisible by three.

 

#Example 1:

#Input: nums = [3,6,5,1,8]
#Output: 18
#Explanation: Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        ## status:cur_i, mod
        ## dp[cur_i][mod] = max sum starting in cur_i with mod 3
        ## prev_0, prev_1, prev2= dp[cur_i-1][0], dp[cur_i-1][1], dp[cur_i-1][2]
        ## dp[cur_i][(prev_0+nums[i])%3] = prev_0+ 
        
#         0, 1,2,3,4
#         [3,6,5,1,8]
#                  i
#         when i in index 3: res=15(3+6+5+1)
#         when i in index 4: res==>18 (3+6+1+8)   dp[i]=max(dp[i-1]+x...)
        
#         ## status: cur_i, mod
#         ##dp[3][1] = up to the 3rd index, what is the max sum having mod3 ==1
        
#         dp[3][1]=0
#         dp[3][2]= 14
#         dp[3][0]= 9
        
#         get:
#         dp[4][1]=10  (0)
#         dp[4][2]=14  (14)
#         dp[4][0]=15   (9)
        
#         dp[-1][0]
        
        
#         0, 14, 9, 
#         0+ nums[4-1](1) =1
#         14+ nums[4-1](1) =15 
#         9+ nums[4-1](1)= 10
        
        
#         1%3=1: dp[4][1]= max(dp[4][1], 1) =1
#         15%3=0: dp[4][0] =max(dp[4][0], 15) =max(9, 15) =15
#         10%3==1: dp[4][1] = max(dp[4][1], 10) =max(1, 10) =10
            
#         dp[4][2] = dp[3][2]
        
        
        ##O(n), O(n)
        dp=[[0, 0, 0] for _ in range(len(nums))]
        for i in range(len(dp)):
            if i==0:
                prev_0, prev_1, prev_2=0, 0, 0
            else:
                prev_0, prev_1, prev_2= dp[i-1][0], dp[i-1][1], dp[i-1][2]
            dp[i][0], dp[i][1], dp[i][2] = prev_0, prev_1, prev_2
            dp[i][(prev_0+nums[i])%3] = max(dp[i][(prev_0+nums[i])%3], prev_0+ nums[i])
            dp[i][(prev_1+nums[i])%3] = max(dp[i][(prev_1+nums[i])%3], prev_1+ nums[i])
            dp[i][(prev_2+nums[i])%3] = max(dp[i][(prev_2+nums[i])%3], prev_2+ nums[i])
        
        return dp[-1][0]
    

# sum%3==0
# find largest sum satisfied sum%3==1, find smalles sum 


        
# 3, 6,  5, 1,  8
# 3, 9, 14, 15, 23

# 0: 
# 1: 
# 2: 



