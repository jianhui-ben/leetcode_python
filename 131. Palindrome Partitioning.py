#131. Palindrome Partitioning
#Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

#A palindrome string is a string that reads the same backward as forward.

 

#Example 1:

#Input: s = "aab"
#Output: [["a","a","b"],["aa","b"]]

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ##backtracking
        self.out=[]
        def backtrack(left, path):
            if not left:
                self.out.append(list(path))
                return
            for i in range(1, len(left)+1):
                if left[:i]==left[:i][::-1]:
                    path.append(left[:i])
                    backtrack(left[i:], path)
                    path.pop()

        backtrack(s, [])
        return self.out
        
