#677. Map Sum Pairs
#Implement the MapSum class:

#MapSum() Initializes the MapSum object.
#void insert(String key, int val) Inserts the key-val pair into the map. If the key already existed, the original key-value pair will be overridden to the new one.
#int sum(string prefix) Returns the sum of all the pairs' value whose key starts with the prefix.
 

#Example 1:

#Input
#["MapSum", "insert", "sum", "insert", "sum"]
#[[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
#Output
#[null, null, 3, null, 5]

#Explanation
#MapSum mapSum = new MapSum();
#mapSum.insert("apple", 3);  
#mapSum.sum("ap");           // return 3 (apple = 3)
#mapSum.insert("app", 2);    
#mapSum.sum("ap");           // return 5 (apple + app = 3 + 2 = 5)
 

#Constraints:

#1 <= key.length, prefix.length <= 50
#key and prefix consist of only lowercase English letters.
#1 <= val <= 1000
#At most 50 calls will be made to insert and sum.
class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.trie = defaultdict()
        

    def insert(self, key: str, val: int) -> None:
        
        cur = self.trie
        for letter in key:
            if letter not in cur:
                cur[letter] = defaultdict()
            cur = cur[letter]
        cur['$'] = val
        
    def sum(self, prefix: str) -> int:
        
        cur = self.trie
        for letter in prefix:
            if letter not in cur:
                return 0
            cur = cur[letter]
        res = 0
        
        def dfs(cur):
            nonlocal res
            if '$' in cur:
                res += cur['$']
            for letter, next_trie in cur.items():
                if letter == '$':
                    continue
                dfs(next_trie)
        
        dfs(cur)
        return res
        
        
        
        
        
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)