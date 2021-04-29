#843. Guess the Word
#This is an interactive problem.

#You are given an array of unique strings wordlist where wordlist[i] is 6 letters long, and one word in this list is chosen as secret.

#You may call Master.guess(word) to guess a word. The guessed word should have type string and must be from the original list with 6 lowercase letters.

#This function returns an integer type, representing the number of exact matches (value and position) of your guess to the secret word. Also, if your guess is not in the given wordlist, it will return -1 instead.

#For each test case, you have exactly 10 guesses to guess the word. At the end of any number of calls, if you have made 10 or fewer calls to Master.guess and at least one of these guesses was secret, then you pass the test case.
# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        ## guess the first word, if 6 return word
        ## elif we get i, we remove all the words inside the wordlist != i similarity
        ## until there is only one word
        
        ## O(N), space O(n)
        
        def similarity(w1, w2):
            k=0
            for i in range(len(w1)):
                if w1[i]==w2[i]:
                    k+=1
            return k
        
        while wordlist:
            import random
            k=random.randint(0,len(wordlist)-1)
            i= master.guess(wordlist[k])
            if i==6:
                return
            temp=[]
            compare = wordlist[k]
            while wordlist:
                if similarity(wordlist[0], compare)==i:
                    temp.append(wordlist[0])
                wordlist.pop(0)
                
            wordlist=temp
            
        
            
        
        