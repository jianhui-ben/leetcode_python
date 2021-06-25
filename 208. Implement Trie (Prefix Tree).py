#208. Implement Trie (Prefix Tree)
#A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

#Implement the Trie class:

#Trie() Initializes the trie object.
#void insert(String word) Inserts the string word into the trie.
#boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
#boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
 

#Example 1:

#Input
#["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
#[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
#Output
#[null, null, true, false, true, null, true]

class TrieNode:
    
    def __init__(self):
        self.children = [None] * 26
        self.end = False
        
class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        O(m) O(m)
        """
        cur_node = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if not cur_node.children[idx]:
                cur_node.children[idx] = TrieNode()
            cur_node = cur_node.children[idx]
        cur_node.end = True
        
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        O(m), O(1)
        """
        cur_node = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if not cur_node.children[idx]:
                return False
            cur_node = cur_node.children[idx]
        return cur_node.end
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur_node = self.root
        for ch in prefix:
            idx = ord(ch) - ord('a')
            if not cur_node.children[idx]:
                return False
            cur_node = cur_node.children[idx]
        return True       
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)