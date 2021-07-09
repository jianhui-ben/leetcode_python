#1235. Maximum Profit in Job Scheduling
#We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

#You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

#If you choose a job that ends at time X you will be able to start another job that starts at time X.

 

#Example 1:



#Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
#Output: 120
#Explanation: The subset chosen is the first and fourth job. 
#Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        """
        binary search nlogn, n: len(endTime)
        """
        jobs = [(endTime[i], startTime[i], profit[i]) for i in range(len(startTime))]
        jobs.sort()
        dp_endtime, dp_profit = [], [] ## (end time, profit at the end time)
        
        def binary_search(arr, target):
            ## last entry in arr where the value is <= the target
            left, right =  0, len(arr) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if arr[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            if right < 0 or arr[right] > target:
                return -1
            return right

        
        for end, start, cur_profit in jobs:
            if not dp_endtime:
                dp_endtime.append(end)
                dp_profit.append(cur_profit)
                
            else:
                ## binary search to find the last entry in dp
                ## where the end time is smaller or equal to start
                i = binary_search(dp_endtime, start)
                
                if i == -1:
                    tot_profit = cur_profit
                else:
                    tot_profit = cur_profit + dp_profit[i]
                
                last_profit = dp_profit[-1]
                if end == dp_endtime[-1] and tot_profit > last_profit:
                    dp_endtime.pop()
                    dp_profit.pop()
                    
                if tot_profit > last_profit:
                    dp_endtime.append(end)
                    dp_profit.append(tot_profit)
        return dp_profit[-1]
                
                
                
            
        
        
        
        
        
        
        
        
        """
        start[1, 2, 3, 3]
        end  [3, 4, 5, 6]
        
        for every start time:
        1: 3
        2: 4
        3: 5, 6
        
        1  2   3   4   5  6
        dp[i]= max profit starting at i
        default: dp[i] = dp[i+1]
        dp[5] = dp[4] =0
        dp[3] = max((3 ->5), (3->6)) = 70
        dp[2] = max((2 -->4)) + dp[4]
        dp[1] = max((1 -- >3) + dp[3]) 
    time: O(len(M * N)), M: max(endTime[i]), N: len(endTime)
    space: O(M)
     """
#         store = defaultdict(list) ## key: startTime; value: [(endTime, profit)]
#         max_time = 0
        
#         for i in range(len(startTime)):
#             ## in case two jobs with the same start and end having different profits
#             store[startTime[i]].append((endTime[i], profit[i]))
#             max_time = max(max_time, endTime[i])
        
#         dp = [0 for _ in range(max_time + 1)]
#         for i in range(max_time - 1, 0, -1):
#             dp[i] = dp[i + 1]
            
#             if i in store:
#                 for endTs, pro in store[i]:
#                     dp[i] = max(dp[i], pro + dp[endTs])
            
#         return dp[1]
    
                
            
            
        
        
        
        
        
    """
        1  2   3   4   5  6
     1  0  0  50   
     2     0   0   10
     3         0   0   40 70
     4             0   0  0
     5                 0  0
     6                    0
        
    dp[i][j] = the max profit from start time i to end time j, where j >= i
    time: (O(N^3)), N= max(endTime)
    space: (O(N^2))
        """
#         store = defaultdict(int) ## key: (startTime, endTime); value: profit
#         max_time = 0
        
#         for i in range(len(startTime)):
#             ## in case two jobs with the same start and end having different profits
#             store[(startTime[i], endTime[i])] = \
#             max(profit[i], store[(startTime[i], endTime[i])])
            
#             max_time = max(max_time, endTime[i])
            
#         dp = [[0 for _ in range(max_time + 1)] for _ in range(max_time + 1)]
#         for i in range(len(dp) - 1, -1, -1):
#             for j in range(i, len(dp)):
#                 if  i == j:
#                     continue
#                 if (i, j) in store:
#                     dp[i][j] = store[(i, j)]
#                 for k in range(i, j):
#                     dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j])
        
#         return dp[0][-1]
                    
                
                
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        