#774. Minimize Max Distance to Gas Station
#You are given an integer array stations that represents the positions of the gas stations on the x-axis. You are also given an integer k.

#You should add k new gas stations. You can add the stations anywhere on the x-axis, and not necessarily on an integer position.

#Let penalty() be the maximum distance between adjacent gas stations after adding the k new stations.

#Return the smallest possible value of penalty(). Answers within 10-6 of the actual answer will be accepted.

 

#Example 1:

#Input: stations = [1,2,3,4,5,6,7,8,9,10], k = 9
#Output: 0.50000


class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        
        
        """
        binary search on monotone stack
        """
        def possible(dis, k):
            needed = 0
            for i in range(len(stations) - 1):
                needed += (stations[i + 1] - stations[i]) // dis
                if needed > k: return False
            return needed <= k
            
        left, right = 0.0, 10.0 ** 8
        
        while right - left >= 10 ** (-6):
            mid = (right + left) / 2.0
            if possible(mid, k):
                right = mid
            else:
                left = mid
        
        return right
        