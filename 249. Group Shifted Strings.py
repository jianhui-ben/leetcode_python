#249. Group Shifted Strings
#We can shift a string by shifting each of its letters to its successive letter.

#For example, "abc" can be shifted to be "bcd".
#We can keep shifting the string to form a sequence.

#For example, we can keep shifting "abc" to form the sequence: "abc" -> "bcd" -> ... -> "xyz".
#Given an array of strings strings, group all strings[i] that belong to the same shifting sequence. You may return the answer in any order.

 

#Example 1:

#Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
#Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]
#Example 2:

#Input: strings = ["a"]
#Output: [["a"]]


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        
        
        def convert(word):
            if len(word) == 1: return '-'
            
            res = ''
            for i in range(1, len(word)):
                
                
                first, second= word[i - 1], word[i]

                if ord(second) >= ord(first):
                    d = ord(second) - ord(first)
                else:
                    d = ord('z') - ord(first) + 1 + ord(second) - 97
                res += str(d) + '_'
            return res
        
        
        stored = defaultdict(list)
        
        for word in strings:
            stored[convert(word)].append(word)
        
        return list(stored.values())
        