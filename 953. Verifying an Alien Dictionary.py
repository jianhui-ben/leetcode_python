#953. Verifying an Alien Dictionary

#In an alien language, surprisingly they also use english lowercase letters,
#but possibly in a different order. The order of the alphabet is some permutation
#of lowercase letters.

#Given a sequence of words written in the alien language, and the order of the 
#alphabet, return true if and only if the given words are sorted lexicographicaly
#in this alien language.

 

#Example 1:

#Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
#Output: true
#Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        stored= {c:i for i, c in enumerate(order)}
        if not words: return None
        for i in range(len(words)-1):
            first, second= words[i], words[i+1]
            for k in range(min(len(first), len(second))):
                if stored[first[k]]>stored[second[k]]:
                    return False
                elif stored[first[k]]<stored[second[k]]:
                    break
                elif k==len(second)-1 and len(first)>len(second):
                    return False
        
        return True
                    