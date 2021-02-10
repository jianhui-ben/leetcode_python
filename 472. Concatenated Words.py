#472. Concatenated Words

#Given a list of words (without duplicates), please write a program that returns all concatenated words in the given list of words.

#A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

 

#Example 1:

#Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
#Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
#Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
#"dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
#"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        ##mem, min optimination
        self.out=[]
        self.mem=collections.defaultdict()
        words=[w for w in words if w!=""]
        if not words: return []
        self.min= min([len(w) for w in words])
        # words.sort(key=lambda x: len(x))
        words=set(words)
        for word in words:
            if self.dfs(word, words):
                self.out.append(word)
        return self.out
    
    def dfs(self, word, words):
        if not word: return False
        if word in self.mem:
            return self.mem[word]
        for k in range(self.min, len(word)+1-self.min):
            sub=word[:k]
            if sub in words and ((word[k:] and word[k:] in words) or self.dfs(word[k:],words)):
                self.mem[word]=True
                return self.mem[word]
        self.mem[word]= False
        return self.mem[word]

    
# class Solution:
#     def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
#         ## set as a mem
#         ## it works excepts some really rare test cases
#         self.out=[]
#         self.mem=set()
        
#         # words.sort(key=lambda x: len(x))
#         words=set([w for w in words if w!=""])
#         for word in words:
#             if self.dfs(word, words):
#                 self.out.append(word)
#         return self.out
    
#     def dfs(self, word, words):
#         if not word: return False
#         if word in self.mem:
#             return True
#         for k in range(1, len(word)+1):
#             sub=word[:k]
#             if sub in words and (word[k:] in words or self.dfs(word[k:],words)):
#                 self.mem.add(word)
#                 return True
#         return False
   
    
        ## brute force: N**M TLE
#         self.out=set()
#         words=set(words)
#         self.dfs(words, "", 0, max([len(i) for i in words]))
#         return list(self.out)
    
#     def dfs(self, words, cur, used, target):
#         if cur in words and used>=2:
#             self.out.add(cur)
#             return
#         elif len(cur)>=target:
#             return 
#         else:
#             for i in words:
#                 self.dfs(words, cur+i,used+1, target)
                

    
        
        