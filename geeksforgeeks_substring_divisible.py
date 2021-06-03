#Count of sub-strings that are divisible by K
https://www.geeksforgeeks.org/count-of-sub-strings-that-are-divisible-by-k/
#Given an integer K and a numeric string str (all the characters are from the range [‘0’, ‘9’]). 
#The task is to count the number of sub-strings of str that are divisible by K.
#Input: str ="33445", K = 11 
#Output: 3 
## brute force will just be O(n**2)

## here is an efficient approach with O(n) using hashmap to save the counts of diffrent reminders


##hashmap approach:
## '445', from right to left: 5: reminder=5, '45': reminder=1, '445': reminder= 5

def countDivisible(s, k):
    res=0
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if int(s[i:j])%k==0:
                res+=1
    return res



def countDivisible(s, k):

    import collections
    reminder=collections.defaultdict(int)
    reminder[0]=1
    res = 0
    for i in range(len(s)-1, -1, -1):
        suffix = int(s[i:])
        res+= reminder[suffix%k]
        reminder[suffix%k]+=1
    return res
    


