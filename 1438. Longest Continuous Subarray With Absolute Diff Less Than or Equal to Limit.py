#1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        ## improved version of sliding window with two deques to get min/max
        ## time O(n), space O(n)
        
        l, r = 0, 0
        from collections import deque        
        #Approach: Using deques as calculating max,min for each subarray is costly
        min_q = deque()
        max_q = deque()
        
        #STEP1: Iterate subarrays using window of l to r 
        while r < len(nums):
            n = nums[r] #Get current element
            
            #STEP2: If current element < last element of min queue, pop it(REPEAT)
            while min_q and n < nums[min_q[-1]]:
                min_q.pop()
            
            #STEP3: If current element > last element of max queue, pop it(REPEAT)
            while max_q and n > nums[max_q[-1]]:
                max_q.pop()
                
            #---- Now queue satisfies insertion of current element ------
            
            #STEP4: Add index of current element to both queues at the last
            min_q.append(r)
            max_q.append(r)
            
            #STEP5: Get max and min values in current subarray
            max_e = nums[max_q[0]]
            min_e = nums[min_q[0]]
            
            #STEP6: If it violates limit, shrink the window from left
            if max_e - min_e > limit:
                l += 1
                #STEP7: We had previously considered the value we discarded, now we need to update our queues. So pop any index before current window
                while min_q and min_q[0] < l:
                    min_q.popleft()
                while max_q and max_q[0] < l:
                    max_q.popleft()
            r += 1
        
        #STEP8 Return the size of the current window.
        return (r-l)
    
    #r - l because r has increased by 1 already, no need to do r-l+1
                    
        
        
        
        
        
        ## sliding window
        ## O(n**2) in worst case, space O(n)
        from collections import deque 
        left, right = 0, 0
        window, win_min, win_max=defaultdict(int), float('inf'), float('-inf')
        out= float('-inf')
        while right<len(nums):
            window[nums[right]]+=1
            win_min=min(win_min, nums[right])
            win_max =max(win_max, nums[right])
            right+=1
            
            while win_max-win_min> limit:
                if window[nums[left]]==1:
                    window.pop(nums[left])
                    if nums[left]==win_min: win_min=min(window.keys())
                    elif nums[left]==win_max: win_max=max(window.keys())     
                else:
                    window[nums[left]]-=1

                left+=1 
            out=max(out, right-left)

        return out
