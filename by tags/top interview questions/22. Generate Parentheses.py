#22. Generate Parentheses

#Given n pairs of parentheses, write a function to generate all combinations
#of well-formed parentheses.

#Example 1:

#Input: n = 3
#Output: ["((()))","(()())","(())()","()(())","()()()"]
#Example 2:

#Input: n = 1
#Output: ["()"]

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.out=[]
        def recursion(left, right, cur_str):
            if left>=0 and right>=0:
                if left==0:
                    cur_str+= right*')'
                    self.out.append(cur_str)
                    return
                if left<right:
                    recursion(left, right-1, cur_str+')')
                recursion(left-1, right, cur_str+'(')
                
        recursion(n, n, '')
        return self.out

