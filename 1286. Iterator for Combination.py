1286. Iterator for Combination
Design the CombinationIterator class:

CombinationIterator(string characters, int combinationLength) Initializes the object with a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
next() Returns the next combination of length combinationLength in lexicographical order.
hasNext() Returns true if and only if there exists a next combination.
 

Example 1:

Input
["CombinationIterator", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[["abc", 2], [], [], [], [], [], []]
Output
[null, "ab", true, "ac", true, "bc", false]

class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        ##backtracking
        ## time O(N * C choose K from N)
        self.all_combo= []
        def backtrack(characters, idx, cur, target):
            if len(cur)==target:
                self.all_combo.append(cur)
                return
            if idx==len(characters):
                return
            for i in range(idx, len(characters)):
                backtrack(characters, i+1, cur+characters[i], combinationLength)    
        backtrack(characters, 0, '', combinationLength)
        
    def next(self) -> str:
        out =self.all_combo.pop(0)
        return out
        

    def hasNext(self) -> bool:
        return len(self.all_combo)>0
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
