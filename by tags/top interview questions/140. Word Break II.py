#140. Word Break II
#Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

#Note:

#The same word in the dictionary may be reused multiple times in the segmentation.
#You may assume the dictionary does not contain duplicate words.
#Example 1:

#Input:
#s = "catsanddog"
#wordDict = ["cat", "cats", "and", "sand", "dog"]
#Output:
#[
#  "cats and dog",
#  "cat sand dog"
#]


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.mem= collections.defaultdict(list)
        wordDict=set(wordDict)
        self.dfs(s, wordDict)
        return [" ".join(i) for i in self.mem[s]]
    
    def dfs(self, s, wordDict):
        if not s: return [[]]
        if s in self.mem:
            return self.mem[s]
        for i in range(1, len(s)+1):
            substring= s[:i]
            if substring in wordDict:
                for k in self.dfs(s[i:], wordDict):
                    self.mem[s].append([substring]+k)                
        return self.mem[s]
        
        
#         ## dfs: TLE
#         self.out=[]
#         wordDict=set(wordDict)
#         self.dfs(s, 0,1, "", wordDict)
#         return [i[1:] for i in self.out]
    
    
#     def dfs(self,  s, start, end, cur, wordDict):
#         if end==len(s) and s[start:end] in wordDict:
#             self.out.append(cur+ " "+ s[start:end])
#             return
#         elif end==len(s):
#             return
#         elif s[start:end] in wordDict:
#             self.dfs(s, end, end+1, cur+ " "+ s[start:end], wordDict)
#         self.dfs(s, start, end+1, cur, wordDict)
        
        
        
        
#           ##top-down dp with memo
#         wordSet = set(wordDict)
#         # table to map a string to its corresponding words break
#         # {string: [['word1', 'word2'...], ['word3', 'word4', ...]]}
#         memo = defaultdict(list)

#         #@lru_cache(maxsize=None)    # alternative memoization solution
#         def _wordBreak_topdown(s):
#             """ return list of word lists """
#             if not s:
#                 return [[]]  # list of empty list

#             if s in memo:
#                 # returned the cached solution directly.
#                 return memo[s]

#             for endIndex in range(1, len(s)+1):
#                 word = s[:endIndex]
#                 if word in wordSet:
#                     # move forwards to break the postfix into words
#                     for subsentence in _wordBreak_topdown(s[endIndex:]):
#                         memo[s].append([word] + subsentence)
#             return memo[s]

#         # break the input string into lists of words list
#         _wordBreak_topdown(s)

#         # chain up the lists of words into sentences.
#         return [" ".join(words) for words in memo[s]]  
