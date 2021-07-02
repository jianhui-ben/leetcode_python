#254. Factor Combinations
#Numbers can be regarded as the product of their factors.

#For example, 8 = 2 x 2 x 2 = 2 x 4.
#Given an integer n, return all possible combinations of its factors. You may return the answer in any order.

#Note that the factors should be in the range [2, n - 1].

 

#Example 1:

#Input: n = 1
#Output: []


class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        """
        backtrackng
        backtrack(n, cur_list, cur_num)
        if cur_num == 1: res.append(cur_list), return
        else:
        for i in range(2, cur_num + 1):
            if cur_num % cur_num == 0: ... 
        """
        out = []
        if n < 4: return []
        
        def backtrack(start, cur_list, cur_num):
            if cur_num == 1:
                if len(cur_list) > 1:
                    out.append(cur_list[:])
                return
            else:
                for i in range(start, int(math.sqrt(cur_num)) + 1):
                    if cur_num % i == 0:
                        out.append(cur_list + [i, cur_num // i])
                        cur_list.append(i)
                        backtrack(i, cur_list, cur_num // i)
                        cur_list.pop()

        backtrack(2, [], n)
        
        return out