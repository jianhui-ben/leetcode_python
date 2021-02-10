#126. Word Ladder II
#Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

#Only one letter can be changed at a time
#Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
#Note:

#Return an empty list if there is no such transformation sequence.
#All words have the same length.
#All words contain only lowercase alphabetic characters.
#You may assume no duplicates in the word list.
#You may assume beginWord and endWord are non-empty and are not the same.
#Example 1:

#Input:
#beginWord = "hit",
#endWord = "cog",
#wordList = ["hot","dot","dog","lot","log","cog"]

#Output:
#[
#  ["hit","hot","dot","dog","cog"],
#  ["hit","hot","lot","log","cog"]
#]


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        
        if not endWord or endWord not in wordList: return []
        ##backtracking and BFS
        ## store the intermediate:
        stored_intermediate=collections.defaultdict(set)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                inter=word[:i]+'*'+word[i+1:]
                stored_intermediate[inter].add(word)
        queue= [[beginWord]]
        find= False
        self.visited=set([beginWord])
        self.out=[]
        while queue and not find:
            find, queue=self.bfs(stored_intermediate, queue, endWord, find)
        if not self.out: return []
        return self.out
    
    ## queue
    def bfs(self, stored_intermediate, queue, endWord, find):
        next_queue=[]
        temp_visited=set()
        for cur_path in queue:
            for i in range(len(cur_path[-1])):
                pattern= cur_path[-1][:i]+'*'+ cur_path[-1][i+1:]
                for next_word in stored_intermediate[pattern]:
                    if next_word==endWord:
                        self.out.append(cur_path+[endWord])
                        find=True
                    if next_word not in self.visited:
                        next_queue.append(cur_path+[next_word])
                        temp_visited.add(next_word)
        self.visited=self.visited.union(temp_visited)
        return (find, next_queue)
