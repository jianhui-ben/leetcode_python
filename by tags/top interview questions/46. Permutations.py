#46. Permutations

#Given an array nums of distinct integers, return all the possible permutations. 
#You can return the answer in any order.

 

#Example 1:

#Input: nums = [1,2,3]
#Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#Example 2:

#Input: nums = [0,1]
#Output: [[0,1],[1,0]]

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.out=[]
        def recusion(cur_arr, left):
            if not left:
                self.out.append(cur_arr)
                return
            for i in left:
                recusion(cur_arr+[i], [k for k in left if k!=i])
                ##avoid duplicates
                # recusion([i]+cur_arr, [k for k in left if k!=i])
        recusion([], nums)

        return self.out

