# 787. Cheapest Flights Within K Stops
# There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.
#
# You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        status: cur_stop, k stops
        if k == 0 and dst in graph[cur_stop]: return graph[cur_stop][dst]
        dp(cur_stop) = min(dp(next_stop, k - 1))

        dijaksa algorithm
        """

        ## create a graph
        graph = [{} for _ in range(n)]
        for flight in flights:
            graph[flight[0]][flight[1]] = flight[2]
        queue, dp = [(0, src, k)], [float('inf') for _ in range(n)]
        while queue:
            cur_cost, cur_stop, stops_left = queue.pop(0)
            dp[cur_stop] = min(dp[cur_stop], cur_cost)

            if cur_stop == dst or stops_left < 0:
                continue

            for next_stop, next_cost in graph[cur_stop].items():
                # print(next_stop, next_cost)
                if next_cost + cur_cost < dp[next_stop]:
                    queue.append((next_cost + cur_cost, next_stop, stops_left - 1))
        return dp[dst] if dp[dst] != float('inf') else -1
