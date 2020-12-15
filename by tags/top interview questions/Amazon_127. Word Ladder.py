#127. Word Ladder


#Given two words (beginWord and endWord), and a dictionary's word list, find the
#length of shortest transformation sequence from beginWord to endWord, such that:

#Only one letter can be changed at a time.
#Each transformed word must exist in the word list.
#Note:

#Return 0 if there is no such transformation sequence.
#All words have the same length.
#All words contain only lowercase alphabetic characters.
#You may assume no duplicates in the word list.
#You may assume beginWord and endWord are non-empty and are not the same.
#Example 1:

#Input:
#beginWord = "hit",
#endWord = "cog",
#wordList = ["hot","dot","dog","lot","log","cog"]

#Output: 5

#Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
#return its length 5.

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        ## bfs using intermediate status
        stored_intermediate={}
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                inter=word[:i]+'*'+word[i+1:]
                if inter in stored_intermediate:
                    stored_intermediate[inter].add(word)
                else:
                    stored_intermediate[inter]=set([word])
        #bfs:
        queue=[(beginWord, 1)]
        visited=set(beginWord)
        while queue:
            word, cur_len= queue.pop(0)
            for i in range(len(word)):
                inter=word[:i]+'*'+word[i+1:]
                if inter in stored_intermediate:
                    for next_word in stored_intermediate[inter]:
                        if next_word==endWord: return cur_len+1
                        if next_word not in visited:
                            queue.append((next_word, cur_len+1))
                            visited.add(next_word)
        return 0
        

#         ###time exceeded
#         def check(s1,s2):
#             return sum([[k for k in s1][i]!=[k for k in s2][i] for i in range(len(s1))])==1
        
        
        
#         ##bfs:
#         changes_stored={}
#         wordList.append(beginWord)
#         for i1 in wordList:
#             changes_stored[i1]=set()
#             for i2 in wordList:
#                 if i1!=i2 and check(i1,i2):
#                     changes_stored[i1].add(i2)
        
#         queue=[(beginWord, 0)]
#         used=[beginWord]
#         out=float('inf')
#         # print(changes_stored)
#         while queue:
#             # print(queue)
#             word, cur_num=queue.pop(0)
            
#             if word in changes_stored:
#                 for next_word in changes_stored[word]:
#                     if next_word==endWord:
#                         return cur_num+2
#                     if next_word not in used:
#                         queue.append((next_word, cur_num+1))
#                         used.append(next_word)
#         if out==float('inf'):
#             return 0
#         else: return out
        
        
        