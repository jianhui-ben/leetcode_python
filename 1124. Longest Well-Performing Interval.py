#1124. Longest Well-Performing Interval
#We are given hours, a list of the number of hours worked per day for a given employee.

#A day is considered to be a tiring day if and only if the number of hours worked is (strictly) greater than 8.

#A well-performing interval is an interval of days for which the number of tiring days is strictly larger than the number of non-tiring days.

#Return the length of the longest well-performing interval.

 

#Example 1:

#Input: hours = [9,9,6,0,6,6,9]
#Output: 3
#Explanation: The longest well-performing interval is [9,9,6].


class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        ##convert to binary
        hours= [-1 if hour<=8 else 1 for hour in hours]
        ## prefix sum:
        pre_sum=0
        prefix_sums=[0]* (len(hours)+1)
        for i in range(len(hours)):
            pre_sum+= hours[i]
            prefix_sums[i+1]=pre_sum
        # print(hours)
        # print(prefix_sums)
        ## binary search:
        candidates, out=[], 0
        for i, v in enumerate(prefix_sums):
            if not candidates or prefix_sums[candidates[-1]]>=v:
                candidates.append(i)
            else:
                ##binary search
                low, high= 0, len(candidates)
                while low< high:
                    mid= (low+high)//2
                    if prefix_sums[candidates[mid]]<v:
                        high=mid
                    else:
                        low=mid+1
                out= max(out, i-candidates[low])
        return out
                
        
        
        ## we need to find interval (i: j) in hours, so prefix_sums[j]-prefix_sums[i]>0
        ## then we want to return max (j-i)
        ## brute force: O(n**2) TLE
        # out=0
        # for i in range(len(hours)):
        #     for j in range(i+1, len(hours)+1):
        #         if prefix_sums[j]>prefix_sums[i]:
        #             # print(j, i)
        #             out=max(out, j-i)
        # return out
    
        ## here we can optimize this search
        ## we can pass some redundant search space and ealy stopping: TLE
        # out, j_temp=0, 0
        # for i in range(len(hours)):
        #     for j in range(j_temp+1, len(hours)+1):
        #         if prefix_sums[j]>prefix_sums[i]:
        #             # print(j, i)
        #             out=max(out, j-i)
        #             j_temp= j
        #     if j_temp==len(hours):
        #         break
        # return out
    
        ## two early stoppings: TLE
        # j_temp, out=0, 0
        # for i in range(len(hours)):
        #     for j in range(len(hours), j_temp, -1):
        #         if prefix_sums[j]>prefix_sums[i]:
        #             out=max(out, j-i)
        #             j_temp= j
        #             break
        #     if j_temp==len(hours):
        #         break
        # return out
        