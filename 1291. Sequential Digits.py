#1291. Sequential Digits
#An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

#Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

 

#Example 1:

#Input: low = 100, high = 300
#Output: [123,234]


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ## similar question to 1215
        ## using backtracking technique
        ## better using sliding window
        out =set()
        def dfs(num):
            nonlocal out
            if num<0 or num >high:
                return 
            if low <= num <= high:
                out.add(num)
            if 0<num%10<9:
                dfs(num*10+num%10+1)
            else: return
        for i in range(10):
            dfs(i)
        return sorted(list(out))
        