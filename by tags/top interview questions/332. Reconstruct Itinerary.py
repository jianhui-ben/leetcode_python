#332. Reconstruct Itinerary

#Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

#Note:

#If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
#All airports are represented by three capital letters (IATA code).
#You may assume all tickets form at least one valid itinerary.
#One must use all the tickets once and only once.
#Example 1:

#Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
#Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        ##hashmap and backtracking
        
        stored= collections.defaultdict(list)
        available_tickets=dict(collections.Counter([(a, b)for a,b in tickets]))
        for fr, to in tickets:
            stored[fr].append(to)
        
        for fr, tos in stored.items():
            stored[fr]=sorted(tos)
            
        ##backtracking(visited, cur_path, stored,  cur_location)
        def dfs(available_tickets, cur_path,  cur_location):
            # print(cur_path)
            if not available_tickets:
                return cur_path
            for next_stop in stored[cur_location]:
                if (cur_location, next_stop) in available_tickets:
                    available_tickets[(cur_location, next_stop)]-=1
                    if available_tickets[(cur_location, next_stop)]==0:
                        available_tickets.pop((cur_location, next_stop))
                    cur_path.append(next_stop)
                    out=dfs(available_tickets, cur_path, next_stop)
                    if out: return out
                    else:
                        if (cur_location, next_stop) in available_tickets:
                            available_tickets[(cur_location, next_stop)]+=1
                        else:
                            available_tickets[(cur_location, next_stop)]=1
                        cur_path.pop()
            return None
        return dfs(available_tickets, ['JFK'], "JFK")