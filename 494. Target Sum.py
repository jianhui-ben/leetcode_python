#494. Target Sum
#You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

#Find out how many ways to assign symbols to make sum of integers equal to target S.

#Example 1:

#Input: nums is [1, 1, 1, 1, 1], S is 3. 
#Output: 5
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        
        ## BFS backwards
        ## time O(2^k), here k is size of the set
        queue=collections.defaultdict(int)
        queue[S] =1
        for i in nums[::-1]:
            temp=collections.defaultdict(int)
            while queue:
                cur_key=list(queue.keys())[0]
                cur_val= queue.pop(cur_key)
                temp[cur_key-i]+=cur_val
                temp[cur_key+i]+=cur_val
            queue=temp
        
        return queue[0]
    
        # backtracking
        # time O(2^n)
        out=0
        if len(nums)==0: return 0
        def backtrack(nums, i, rest):
            nonlocal out
            if len(nums) ==i:
                if rest==0:
                    out+=1
                return
            for op in [1, -1]:
                rest-=op*nums[i]
                backtrack(nums, i+1, rest)
                rest +=op*nums[i]

        backtrack(nums, 0, S)
        return out
    
        ##dp can improve the backtracking and reduce the redundant subproblems
        ## we can store (i, rest) into mem
        ## time O(n**2)
        mem=dict()
        if len(nums)==0: return 0
        def dp(nums, i, rest):
            if (i, rest) in mem: return mem[(i, rest)]
            if len(nums) ==i:
                if rest==0:
                    return 1
                return 0
            
            mem[(i, rest)]=dp(nums, i+1, rest-nums[i])+dp(nums, i+1, rest+nums[i])
            return mem[(i, rest)]
        return dp(nums, 0, S)