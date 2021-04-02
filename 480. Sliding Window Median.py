#480. Sliding Window Median
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        ## sliding window +sort window
        ## time O(n *  klogk)
        left, right= 0, 0
        out=[]
        while right<len(nums):
            right+=1
            # heapq.heappush(temp, nums[right])
            while right-left>k:
                left+=1
                heapq.heappop(temp)
            if right-left==k:
                if k%2==1:
                    temp=sorted(nums[left:right])
                    out.append(temp[k//2])
                else:
                    temp=sorted(nums[left:right])
                    out.append(float(temp[k//2]+temp[k//2-1])/2)
        return out
        
