#345. Reverse Vowels of a String

#Write a function that takes a string as input and reverse only the vowels of a string.

#Example 1:

#Input: "hello"
#Output: "holle"


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel=set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        l= [i for i in s if i in vowel]
        ans= ''
        for k in s:
            if k in vowel:
                ans+= str(l.pop())
            else:
                ans+=k
        assert not l
        return ans