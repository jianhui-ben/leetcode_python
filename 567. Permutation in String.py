#567. Permutation in String
#Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

 

#Example 1:

#Input: s1 = "ab" s2 = "eidbaooo"
#Output: True
#Explanation: s2 contains one permutation of s1 ("ba").


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ## idea 1: order dict to store s1
        ## time O(n), space O(n)
        stored=dict(collections.Counter(s1))
        left, right= 0, 0
        while right<len(s2):
            if s2[right] in stored:
                if stored[s2[right]]==1:
                    stored.pop(s2[right])
                else:
                    stored[s2[right]]-=1
                right+=1
            else:
                if left==right:
                    right+=1
                elif s2[left] in stored:
                    stored[s2[left]]+=1
                else:
                    stored[s2[left]]=1
                left+=1
            if not stored: return True
        return False

        ## idea 2: use backtracking to get all permutations
        ## time O(N!)
        
        