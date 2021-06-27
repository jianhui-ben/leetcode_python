#243. Shortest Word Distance
#Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2, return the shortest distance between these two words in the list.

 

#Example 1:

#Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
#Output: 3
#Example 2:

#Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
#Output: 1


class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        ## one pass + stack (O(n), O(1))
        
        idx_1, idx_2, res = -1, -1, float('inf')
        for i, word in enumerate(wordsDict):
            if word == word1:
                idx_1 = i
            elif word == word2:
                idx_2 = i
            if idx_1 > -1 and idx_2 > -1:
                res = min(res, abs(idx_1 - idx_2))
        return res
        
        
        
        
#         ## two pointer
#         ## O(n), O(n)
#         pos_1, pos_2 = [], []
        
#         for i,  word in enumerate(wordsDict):
#             if word == word1:
#                 pos_1.append(i)
#             elif word == word2:
#                 pos_2.append(i)
                
#         idx_1, idx_2 = 0, 0
#         res = float('inf')
#         while idx_1 < len(pos_1) and idx_2 < len(pos_2):
            
#             res = min(res, abs(pos_1[idx_1] - pos_2[idx_2]))
            
#             if pos_1[idx_1] < pos_2[idx_2]:
#                 idx_1 += 1
#             else:
#                 idx_2 += 1
                
#         return res
            
            
        
        
