# 1094. Car Pooling
# There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).
#
# You are given the integer capacity and an array trips where trip[i] = [numPassengersi, fromi, toi] indicates that the ith trip has numPassengersi passengers and the locations to pick them up and drop them off are fromi and toi respectively. The locations are given as the number of kilometers due east from the car's initial location.
#
# Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """
        O(n)
        """

        stops = [0 for _ in range(1001)]

        for trip in trips:
            people, start, end = trip
            stops[start] += people
            stops[end] -= people
        cur = 0
        for i in range(len(stops)):
            cur += stops[i]
            if cur > capacity:
                return False
        return True
