#520. Detect Capital
#Given a word, you need to judge whether the usage of capitals in it is right or not.

#We define the usage of capitals in a word to be right when one of the following cases holds:

#All letters in this word are capitals, like "USA".
#All letters in this word are not capitals, like "leetcode".
#Only the first letter in this word is capital, like "Google".
#Otherwise, we define that this word doesn't use capitals in a right way.
 

#Example 1:

#Input: "USA"
#Output: True

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        i=1
        if not word[0].isupper():
            while i<len(word):
                if word[i].isupper():
                    return False
                i+=1
        else:
            while i<len(word):
                if i==1:
                    second_capital= word[i].isupper()
                else:
                    if word[i].isupper()!=second_capital:
                        return False
                i+=1
                    
        return True
