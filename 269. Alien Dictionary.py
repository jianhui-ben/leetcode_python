#269. Alien Dictionary
#There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.

#You are given a list of strings words from the alien language's dictionary, where the strings in words are sorted lexicographically by the rules of this new language.

#Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there is no solution, return "". If there are multiple solutions, return any of them.

#A string s is lexicographically smaller than a string t if at the first letter where they differ, the letter in s comes before the letter in t in the alien language. If the first min(s.length, t.length) letters are the same, then s is smaller if and only if s.length < t.length.

 

#Example 1:

#Input: words = ["wrt","wrf","er","ett","rftt"]
#Output: "wertf"


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        '''
        topological sort
        t -> f
        w -> e 
        e ->r
        w ->r
        r -> t
        '''
        store_order = defaultdict(set) #key: letter l; value: letters after l
        store_degree = defaultdict(int) #key: letter l; value: degrees of l
        
        rules = set()
        
        
        for i in range(len(words)-1):
            
            for j in range(i+1, len(words)):
                
                small_word, large_word = words[i], words[j]
                
                if len(small_word) > len(large_word) \
                and small_word[:len(large_word)] == large_word:
                    return ""
                
                
                for k in range(min(len(small_word), len(large_word))):
                    if small_word[k] == large_word[k]:
                        continue
                    rules.add((small_word[k], large_word[k]))
                    break
          
        for small_l, large_l in rules:
            store_degree[large_l] += 1
            store_order[small_l].add(large_l)
            
        # ["wrt","wrf","er","ett","rftt"]  
        unique_letters = set()
        for w in words:
            for l in w:
                unique_letters.add(l)
                
        out, queue = '', []
        for l in unique_letters:
            if l not in store_order and l not in store_degree:
                # it doesn't matter where to be put
                out += l
            elif l not in store_degree and l in store_order:
                ## it's a 0-degree letter
                queue.append(l)
        
        ## start topological sort
        while queue:
            cur_l = queue.pop(0)
            out += cur_l
            for larger_l in store_order[cur_l]:
                store_degree[larger_l] -= 1
                if store_degree[larger_l] == 0:
                    queue.append(larger_l)
        if len(out) == len(unique_letters):
            return out
        return ""
                    