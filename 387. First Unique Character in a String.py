#Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

#Examples:

#s = "leetcode"
#return 0.

#s = "loveleetcode",
#return 2.
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        ##method 1: list.count
#         uni=[]
#         full=[]
#         for c in s:
#             if c not in uni:
#                 uni.append(c)
#             full.append(c)
            
#         for i in uni:
#             if full.count(i)==1:
#                 return full.index(i)
#         return -1
    
    # method 2: build hash map : character and how often it appears
        count = collections.Counter(s)
        
        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx     
        return -1
            
 