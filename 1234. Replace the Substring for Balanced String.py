#1234. Replace the Substring for Balanced String
#You are given a string containing only 4 kinds of characters 'Q', 'W', 'E' and 'R'.

#A string is said to be balanced if each of its characters appears n/4 times where n is the length of the string.

#Return the minimum length of the substring that can be replaced with any other string of the same length to make the original string s balanced.

#Return 0 if the string is already balanced.

 

#Example 1:

#Input: s = "QWER"
#Output: 0
#Explanation: s is already balanced.

class Solution:
    def balancedString(self, s: str) -> int:
        target = collections.Counter()
        for i, fre in Counter(s).items():
            if fre > len(s) / 4:
                target[i] = fre - len(s) / 4
        
        if not target: return 0
        
        left, right, cur_store, ans = 0, 0, defaultdict(int), len(s)
        
        def contain(cur_store, target):
            for i, fre in target.items():
                if cur_store[i] < fre:
                    return False
            return True
        
        while right < len(s):
            cur_store[s[right]] += 1
            right += 1
            
            while contain(cur_store, target):
                ans = min(ans, right - left)
                cur_store[s[left]] -= 1
                left += 1
                
        return ans
        