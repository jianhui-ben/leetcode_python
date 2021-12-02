# 1109. Corporate Flight Bookings
# There are n flights that are labeled from 1 to n.
#
# You are given an array of flight bookings bookings, where bookings[i] = [firsti, lasti, seatsi] represents a booking for flights firsti through lasti (inclusive) with seatsi seats reserved for each flight in the range.
#
# Return an array answer of length n, where answer[i] is the total number of seats reserved for flight i.

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        """
        prefix difference
        """
        out = [0 for _ in range(n)]
        for booking in bookings:
            start, end, seats = booking
            out[start - 1] += seats
            if end < len(out):
                out[end] -= seats

        for i in range(1, len(out)):
            out[i] += out[i - 1]
        return out
