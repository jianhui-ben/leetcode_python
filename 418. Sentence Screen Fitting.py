#418. Sentence Screen Fitting
#Given a rows x cols screen and a sentence represented as a list of strings, return the number of times the given sentence can be fitted on the screen.

#The order of words in the sentence must remain unchanged, and a word cannot be split into two lines. A single space must separate two consecutive words in a line.

 

#Example 1:

#Input: sentence = ["hello","world"], rows = 2, cols = 8
#Output: 1
#Explanation:
#hello---
#world---
#The character '-' signifies an empty space on the screen.
#Example 2:

#Input: sentence = ["a", "bcd", "e"], rows = 3, cols = 6
#Output: 2
#Explanation:
#a-bcd- 
#e-a---
#bcd-e-
#The character '-' signifies an empty space on the screen.


class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        
        """
        dp(i) = (next_index, cnt)
        Time: O(len(sentence) * cols + rows)
        Space: O(len(sentence))
        """
        def dp(i):
            if self.mem[i] != None:
                return self.mem[i]
            
            nonlocal cols
            last_i = i
            cur_col, cnt = 0, 0
            while cur_col + len(sentence[i]) <= cols:
                cur_col += len(sentence[i]) + 1
                i += 1
                
                if i == len(sentence):
                    i = 0
                    cnt += 1
            self.mem[last_i] = (i, cnt)
            return i, cnt
        
        i, out = 0, 0
        self.mem = [None] * len(sentence)
        
        for r in range(rows):
            
            next_index, cnt = dp(i)
            i = next_index
            out += cnt
            
        return out
        
        
        