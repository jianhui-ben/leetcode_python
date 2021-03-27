#186. Reverse Words in a String II

class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        ## two pointer:
        ## time O(n), space O(1)
        def swamp(s, start, end):
            while start<end:
                s[end], s[start]=s[start], s[end]
                end-=1
                start+=1
        
        swamp(s, 0, len(s)-1)
        start=0
        for end in range(1, len(s)):
            if s[end]==" ":
                swamp(s, start, end-1)
                start=end+1
        swamp(s, start, len(s)-1)
        