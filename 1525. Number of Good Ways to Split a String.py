#1525. Number of Good Ways to Split a String
#You are given a string s, a split is called good if you can split s into 2 non-empty strings p and q where its concatenation is equal to s and the number of distinct letters in p and q are the same.

#Return the number of good splits you can make in s.

 

#Example 1:

#Input: s = "aacaba"
#Output: 2
#Explanation: There are 5 ways to split "aacaba" and 2 of them are good. 
#("a", "acaba") Left string and right string contains 1 and 3 different letters respectively.
#("aa", "caba") Left string and right string contains 1 and 3 different letters respectively.
#("aac", "aba") Left string and right string contains 2 and 2 different letters respectively (good split).
#("aaca", "ba") Left string and right string contains 2 and 2 different letters respectively (good split).
#("aacab", "a") Left string and right string contains 3 and 1 different letters respectively.


class Solution:
    def numSplits(self, s: str) -> int:
        
        """
        a: 4
        c: 1
        b: 1
        
        left and right sliding window into hashtable
        """
        
        right_window = collections.Counter(s)
        left_window = defaultdict(int)
        
        out = 0
        for letter in s:
            if len(right_window) < len(left_window):
                break
        
            left_window[letter] += 1
            right_window[letter] -= 1
            if not right_window[letter]: 
                right_window.pop(letter)
            if len(left_window) == len(right_window):
                out += 1
        return out