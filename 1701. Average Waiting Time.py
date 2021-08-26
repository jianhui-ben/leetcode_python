#1701. Average Waiting Time
#There is a restaurant with a single chef. You are given an array customers, where customers[i] = [arrivali, timei]:

#arrivali is the arrival time of the ith customer. The arrival times are sorted in non-decreasing order.
#timei is the time needed to prepare the order of the ith customer.
#When a customer arrives, he gives the chef his order, and the chef starts preparing it once he is idle. The customer waits till the chef finishes preparing his order. The chef does not prepare food for more than one customer at a time. The chef prepares food for customers in the order they were given in the input.

#Return the average waiting time of all customers. Solutions within 10-5 from the actual answer are considered accepted.

 

#Example 1:

#Input: customers = [[1,2],[2,5],[4,3]]
#Output: 5.00000
#Explanation:
#1) The first customer arrives at time 1, the chef takes his order and starts preparing it immediately at time 1, and finishes at time 3, so the waiting time of the first customer is 3 - 1 = 2.
#2) The second customer arrives at time 2, the chef takes his order and starts preparing it at time 3, and finishes at time 8, so the waiting time of the second customer is 8 - 2 = 6.
#3) The third customer arrives at time 4, the chef takes his order and starts preparing it at time 8, and finishes at time 11, so the waiting time of the third customer is 11 - 4 = 7.
#So the average waiting time = (2 + 6 + 7) / 3 = 5.

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        """
        [[1,2], [2,5], [4,3]]
                  ^
        
        chief = 0
              = max(1, 0) + 2 = 3
              = max(3,2) + 5 = 8
              = max(8, 4) + 3 = 11
        
        first customer: max(0, 1) - 1 + 2 = 2 min
        second customer: max(3, 2) - 2 + 5 = 6 min
        third customer: max(4, 8) - 4 + 3 = 7 min
        
        """
        chief_ava_time, tot_wait = 0, 0
        
        for arr_time, cook_time in customers:
            # tot_wait += max(chief_ava_time, arr_time) - arr_time + cook_time
            # chief_ava_time = max(chief_ava_time, arr_time) + cook_time
            
            chief_ava_time = max(chief_ava_time, arr_time) + cook_time
            tot_wait += chief_ava_time - arr_time
            
        
        return tot_wait / len(customers)
            