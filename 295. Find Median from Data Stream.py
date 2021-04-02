#295. Find Median from Data Stream
class MedianFinder:
    
    ## heap: two heaps:
    ## time O(log n) in add and O(1) in get_median, space O(n)
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small_half, self.large_half=[],[]
        self.len=0
        

    def addNum(self, num: int) -> None:
        import heapq
        if not self.large_half or num>= self.large_half[0]:
            heapq.heappush(self.large_half, num)
        else:
            heapq.heappush(self.small_half, -num)

        self.len+=1
        while abs(len(self.large_half)-len(self.small_half))>1:
            if len(self.large_half)>len(self.small_half):
                smallest_in_largest=heapq.heappop(self.large_half)
                heapq.heappush(self.small_half, -smallest_in_largest)
            else:
                largest_in_small=heapq.heappop(self.small_half)
                heapq.heappush(self.large_half, -largest_in_small)                

    def findMedian(self) -> float:
        if self.len%2==1:
            if len(self.large_half)>len(self.small_half): return self.large_half[0]
            else: return -self.small_half[0]
        else:
            return float(self.large_half[0]-self.small_half[0])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
