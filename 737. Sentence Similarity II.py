#737. Sentence Similarity II
#Given two sentences words1, words2 (each represented as an array of strings), and a list of similar word pairs pairs, determine if two sentences are similar.

#For example, words1 = ["great", "acting", "skills"] and words2 = ["fine", "drama", "talent"] are similar, if the similar word pairs are pairs = [["great", "good"], ["fine", "good"], ["acting","drama"], ["skills","talent"]].

#Note that the similarity relation is transitive. For example, if "great" and "good" are similar, and "fine" and "good" are similar, then "great" and "fine" are similar.

#Similarity is also symmetric. For example, "great" and "fine" being similar is the same as "fine" and "great" being similar.

#Also, a word is always similar with itself. For example, the sentences words1 = ["great"], words2 = ["great"], pairs = [] are similar, even though there are no specified similar word pairs.

#Finally, sentences can only be similar if they have the same number of words. So a sentence like words1 = ["great"] can never be similar to words2 = ["doubleplus","good"].

class Solution:
    ## union find
    ## time O(P+ len(words list)* P)
    ## space O(len(unique words in pairs))
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if words1==words2: return True
        if not words1 or not words2 or len(words1)!=len(words2):
            return False
        
        all_words= collections.defaultdict()
        for a,b in pairs:
            all_words[a]=-1
            all_words[b]=-1
        for a,b in pairs:
            self.union(all_words, a,b)
            
        for i in range(len(words1)):
            a,b =words1[i], words2[i]
            if a==b: continue
            if self.find(all_words, a)!=self.find(all_words, b):
                return False
        return True
    
    
    def find(self, parents, i):
        if i not in parents: return None
        if parents[i]==-1:
            return i
        return self.find(parents, parents[i])

    def union(self, parents, a,b):
        a_p=self.find(parents, a)
        b_p=self.find(parents, b)
        if a_p!=b_p:
            parents[a_p]=b_p
            
    ##second method is to use queue to do dfs
        
        
            
            
        
        
        
    
        
        
        
