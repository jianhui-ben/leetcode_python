#239. Sliding Window Maximum
#You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

#Return the max sliding window.

 

#Example 1:

#Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
#Output: [3,3,5,5,6,7]
#Explanation: 
#Window position                Max
#---------------               -----
#[1  3  -1] -3  5  3  6  7       3
# 1 [3  -1  -3] 5  3  6  7       3
# 1  3 [-1  -3  5] 3  6  7       5
# 1  3  -1 [-3  5  3] 6  7       5
# 1  3  -1  -3 [5  3  6] 7       6
# 1  3  -1  -3  5 [3  6  7]      7


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ##brute force 1:
        ## time O(n* K), space O(n)
        # if len(nums)<k: return [max(nums)]
        # out=[]
        # for i in range(k-1, len(nums)):
        #     out.append(max(nums[i-k+1:i+1]))
        # return out
    
        ##brute force 2: use a heap: time O(n*log k), space O(n)
#         if len(nums)<k: return [max(nums)]
#         import heapq
        
#         out=[]
#         for i in range(k-1, len(nums)):
#             h=[-i for i in nums[i-k+1:i+1]]
#             heapq.heapify(h)
#             out.append(-h[0])
#         return out
        
        ##use a deque: time O(n)
        if not nums or k==0: return []
        if len(nums)<k: return [max(nums)]
        
        import collections
        d, out=deque(), []
        for i in range(len(nums)):
            if d and d[0]== i-k:
                d.popleft()
            while d and nums[i]>nums[d[-1]]:
                d.pop()
            d.append(i)
            if i>=k-1:
                out.append(nums[d[0]])
        return out
