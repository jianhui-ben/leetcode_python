#1375 · Substring With At Least K Distinct Characters
#Description
#Given a string S with only lowercase characters.

#Return the number of substrings that contains at least k distinct characters.

#10 ≤ length(S) ≤ 1,000,00010≤length(S)≤1,000,000
#1 ≤ k ≤ 261≤k≤26
#Example
#Example 1:

#Input: S = "abcabcabca", k = 4
#Output: 0
#Explanation: There are only three distinct characters


class Solution:
    """
    @param s: a string
    @param k: an integer
    @return: the number of substrings there are that contain at least k distinct characters
    """



    def kDistinctCharacters(self, s, k):
        # Write your code here
        import collections
        window = collections.defaultdict(int)
        left, right = 0, 0
        ans=0
        while right< len(s):
            window[s[right]]+=1
            right+=1
            while left<len(s) and len(window)>=k:
                ans+=len(s)- right+1
                window[s[left]]-=1
                if window[s[left]]==0:
                    window.pop(s[left])
                left+=1
        return ans