#211. Design Add and Search Words Data Structure

#Design a data structure that supports adding new words and finding if a string matches any previously added string.

#Implement the WordDictionary class:

#WordDictionary() Initializes the object.
#void addWord(word) Adds word to the data structure, it can be matched later.
#bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 
##using a trie
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie={}
        
    def addWord(self, word: str) -> None:
        # time O(len(word))
        node= self.trie
        for i in word:
            if i not in node:
                node[i]={}
            node=node[i]
        node['$']= True

    ## recursive; actually iterative should be faster
    def search(self, word: str) -> bool:
        node=self.trie
        def dfs(node, word):
            if not word:
                return '$' in node
            if word[0]!= '.':
                    if word[0] not in node: return False
                    else: return dfs(node[word[0]], word[1:])
            else:
                for first, after in node.items():
                    if first!= '$' and dfs(after, word[1:]):
                        return True
                return False
        return dfs(node, word)
                    


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

# ## using a hashtable:
# class WordDictionary:
#     def __init__(self):
#         self.d = defaultdict(set)


#     def addWord(self, word: str) -> None:
#         self.d[len(word)].add(word)


#     def search(self, word: str) -> bool:
#         m = len(word)
#         for dict_word in self.d[m]:
#             i = 0
#             while i < m and (dict_word[i] == word[i] or word[i] == '.'):
#                 i += 1
#             if i == m:
#                 return True
#         return False




