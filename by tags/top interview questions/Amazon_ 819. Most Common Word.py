#819. Most Common Word
#Given a paragraph and a list of banned words, return the most frequent 
#word that is not in the list of banned words.  It is guaranteed there 
#is at least one word that isn't banned, and that the answer is unique.

#Words in the list of banned words are given in lowercase, and free of
#punctuation.  Words in the paragraph are not case sensitive.  The answer is in lowercase.

 

#Example:

#Input: 
#paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
#banned = ["hit"]
#Output: "ball"
#Explanation: 
#"hit" occurs 3 times, but it is a banned word.
#"ball" occurs twice (and no other word does), so it is the most frequent non-banned 
#word in the paragraph. 
#Note that words in the paragraph are not case sensitive,
#that punctuation is ignored (even if adjacent to words, such as "ball,"), 
#and that "hit" isn't the answer even though it occurs more because it is banned.


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        l=[]
        word=''
        for i in paragraph:
            if i.isalpha():
                word+=i.lower()
            elif word!='':
                l.append(word)
                word=''
        if word!='': l.append(word)
        
        # l="".join([i.lower() for i in paragraph if i.isalpha() or i==" "]).split()
        hashtable= {}
        for i in l:
            if i not in banned:
                if i not in hashtable:
                    hashtable[i]=1
                else:
                    hashtable[i]+=1
        
        return sorted(hashtable.items(), reverse=True, key=lambda i: i[1])[0][0]
        