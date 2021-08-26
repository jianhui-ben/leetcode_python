#809. Expressive Words

#Sometimes people repeat letters to represent extra feeling. For example:

#"hello" -> "heeellooo"
#"hi" -> "hiiii"
#In these strings like "heeellooo", we have groups of adjacent letters that are all the same: "h", "eee", "ll", "ooo".

#You are given a string s and an array of query strings words. A query word is stretchy if it can be made to be equal to s by any number of applications of the following extension operation: choose a group consisting of characters c, and add some number of characters c to the group so that the size of the group is three or more.

#For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", but we cannot get "helloo" since the group "oo" has a size less than three. Also, we could do another extension like "ll" -> "lllll" to get "helllllooo". If s = "helllllooo", then the query word "hello" would be stretchy because of these two extension operations: query = "hello" -> "hellooo" -> "helllllooo" = s.
#Return the number of query strings that are stretchy.

 

#Example 1:

#Input: s = "heeellooo", words = ["hello", "hi", "helo"]
#Output: 1
#Explanation: 
#We can extend "e" and "o" in the word "hello" to get "heeellooo".
#We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.

class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        out = 0
        
        
        def compare(s, word):
            """
            heeellooo
            hello
            """
            s_i, w_i = 0, 0
            while s_i < len(s):
                if w_i >= len(word) or s[s_i] != word[w_i]:
                    return False
                
                freq_s, freq_w = 1, 1
                while s_i + 1 < len(s) and s[s_i + 1] == s[s_i]:
                    s_i += 1
                    freq_s += 1
                    
                while w_i + 1 < len(word) and word[w_i + 1] == word[w_i]:
                    w_i += 1
                    freq_w += 1
                
                if freq_s >= 3 and freq_w > freq_s:
                    return False
                if freq_s < 3 and freq_w != freq_s:
                    return False
                s_i += 1
                w_i += 1
                
            return w_i == len(word)
           
        
        for word in words:
            if compare(s, word):
                out += 1
                
        return out