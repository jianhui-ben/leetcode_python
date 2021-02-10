#767. Reorganize String

#Given a string S, check if the letters can be rearranged so that 
#two characters that are adjacent to each other are not the same.

#If possible, output any possible result.  If not possible, return the empty string.

#Example 1:

#Input: S = "aab"
#Output: "aba"

class Solution:
    def reorganizeString(self, S: str) -> str:
        
        import collections
        counts=collections.Counter(S)
        
        out=""
        max_heap= [(-count, i) for i, count in counts.items()]
        heapq.heapify(max_heap)
        while len(max_heap)>1:
            count1, i1= heapq.heappop(max_heap)
            out+=i1
            count1+=1
            count2, i2= heapq.heappop(max_heap)
            out+=i2
            count2+=1
            if count1<0:
                heapq.heappush(max_heap, (count1, i1))
            if count2<0:
                heapq.heappush(max_heap, (count2, i2))

        if not max_heap: return out
        elif max_heap[0][0]<-1:
            return ""
        else: return out+max_heap[0][1]
        
    ## a very smart way of doing that:
class Solution(object):
    def reorganizeString(self, S):
        N = len(S)
        A = []
        for c, x in sorted((S.count(x), x) for x in set(S)):
            if c > (N+1)/2: return ""
            A.extend(c * x)
        ans = [None] * N
        ans[::2], ans[1::2] = A[N/2:], A[:N/2]
        return "".join(ans)
