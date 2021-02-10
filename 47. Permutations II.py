#47. Permutations II
#Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

#Example 1:

#Input: nums = [1,1,2]
#Output:
#[[1,1,2],
# [1,2,1],
# [2,1,1]]
#Example 2:

#Input: nums = [1,2,3]
#Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 
class Solution:
    ## time O(n**2), space O(n)
    
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.out=[]
        import collections
        left=dict(collections.Counter(nums))
        self.dfs([], left)
        return self.out
    
    def dfs(self, cur, left):
        if not left:
            self.out.append(cur)
            return
        available=list(left.keys())
        for cur_val in available:
            if left[cur_val]==1:
                left.pop(cur_val)
            else:
                left[cur_val]-=1
            self.dfs([cur_val]+cur, left)
            
            if cur_val in left:
                left[cur_val]+=1
            else:
                left[cur_val]=1
