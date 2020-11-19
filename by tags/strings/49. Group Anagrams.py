#49. Group Anagrams
#Given an array of strings strs, group the anagrams together. You can return 
#the answer in any order.

#An Anagram is a word or phrase formed by rearranging the letters of a different
#word or phrase, typically using all the original letters exactly once.

 

#Example 1:

#Input: strs = ["eat","tea","tan","ate","nat","bat"]
#Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
#Example 2:

#Input: strs = [""]
#Output: [[""]]


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out={}
        for word in strs:
            dic= {}
            for c in word:
                if c in dic: dic[c]+=1
                else: dic[c]=1
            label= result = '_'.join('{}{}'.format(*p) for p in sorted(dic.items()))
            if label not in out:
                out[label]= [word]
            else:
                out[label].append(word)
        return [group for group in out.values()]
        
