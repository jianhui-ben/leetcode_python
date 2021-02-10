#77. Combinations
#Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

#You may return the answer in any order.

 

#Example 1:

#Input: n = 4, k = 2
#Output:
#[
#  [2,4],
#  [3,4],
#  [2,3],
#  [1,2],
#  [1,3],
#  [1,4],
#]

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        #bit mask:
        if k>n or k<=0: return None
        start= "1"* k
        end= "1"*k+ "0"*(n-k)
        options= [i for i in range(1, n+1)]
        out=[]
        
        for i in range(int(start, 2),int(end, 2)+1):
            cur_sel= bin(i)[2:]
            if len(cur_sel)<n: 
                cur_sel= "0"*(n-len(cur_sel))+ cur_sel
            if cur_sel.count('1')==k:
                out.append([options[ind] for ind, val in enumerate(cur_sel) if val=="1"])
        return out
                
        
        # ##recursive
        # if k>n or k<=0: return None
        # self.out=[]
        # arr= [i for i in range(1, n+1)]
        # def recur(cur, ind):
        #     if ind<=n:
        #         if len(cur)==k:
        #             self.out.append(cur)
        #             return
        #         for i in range(ind, n):
        #             recur(cur+[arr[i]], i+1)
        # recur([], 0)
        # return self.out