#244. Shortest Word Distance II
#Design a data structure that will be initialized with a string array, and then it should answer queries of the shortest distance between two different strings from the array.

#Implement the WordDistance class:

#WordDistance(String[] wordsDict) initializes the object with the strings array wordsDict.
#int shortest(String word1, String word2) returns the shortest distance between word1 and word2 in the array wordsDict.


class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.words_pos = defaultdict(list)
        for i, word in enumerate(wordsDict):
            self.words_pos[word].append(i)
        

    def shortest(self, word1: str, word2: str) -> int:
        """
        [1, 3, 4]
         i
        [2, 5]
         j
         two pointer O(n)
        """
        word1_pos, word2_pos = self.words_pos[word1], self.words_pos[word2]
        i, j = 0, 0 
        res = float('inf')
        while i < len(word1_pos) and j < len(word2_pos):
            res = min(res, abs(word1_pos[i] - word2_pos[j]))
            
            if word1_pos[i] > word2_pos[j]:
                j += 1
            else:
                i += 1
        
        return res
            
        
        
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)