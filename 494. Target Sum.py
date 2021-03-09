#494. Target Sum
#You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

#Find out how many ways to assign symbols to make sum of integers equal to target S.

#Example 1:

#Input: nums is [1, 1, 1, 1, 1], S is 3. 
#Output: 5

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        
        ## BFS backwards
        ## time O()
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