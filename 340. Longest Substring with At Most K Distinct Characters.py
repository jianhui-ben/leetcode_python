#340. Longest Substring with At Most K Distinct Characters


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        ## use a dict to store the counts of letters
        ## use a liding window to get the substring
        ## if counts of distinct characters>k, left+=1
        ## else: right+=1
        
        ## O(2 * n), space: O(n)
        
        out=0
        left, right=0, 0
        stored= collections.defaultdict(int)
        while right<len(s):
            stored[s[right]]+=1
            right+=1
            if len(stored)<=k:
                out= max(out, right-left)
            else:
                while len(stored)>k:
                    if stored[s[left]]==1:
                        stored.pop(s[left])
                    else:
                        stored[s[left]]-=1
                    left+=1
        return out
                    
