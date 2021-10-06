#1248. Count Number of Nice Subarrays
#Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

#Return the number of nice sub-arrays.

 

#Example 1:

#Input: nums = [1,1,2,1,1], k = 3
#Output: 2
#Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        """
        prefix count + hashtable
        [1,1,2,1,1]
         0,1,2,2,3,4
         
         goal: 3
        
        """
        prefix = [0]
        for i in nums:
            prefix.append(prefix[-1] + i % 2)
        count, ans = defaultdict(int), 0
        for i in prefix:
            ans += count[i - k]
            count[i] += 1
        return ans
        
        
        
        
        
        
        """
        sliding window
        - we find # of subarray with at most K odd numbers
        - we find # of subarrary with at most k-1 odd numbers
        -minus
        """
        def atMost(nums, k):
            left, right, ans, cur_cnt = 0, 0, 0, 0
            while right < len(nums):
                cur_cnt += nums[right] % 2
                right += 1
                
                while left < right and cur_cnt > k:
                    cur_cnt -= nums[left] % 2
                    left += 1
                
                ans += right - left
            return ans
        
        return atMost(nums, k) - atMost(nums, k - 1)
    
    