
#The count-and-say sequence is the sequence of integers with the first five terms as following:

#1.     1
#2.     11
#3.     21
#4.     1211
#5.     111221
#1 is read off as "one 1" or 11.
#11 is read off as "two 1s" or 21.
#21 is read off as "one 2, then one 1" or 1211.

#Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say 
#sequence. You can do so recursively, in other words from the previous member read off the digits, 
#counting the number of digits in groups of the same digit.

#Note: Each term of the sequence of integers will be represented as a string.

 

#Example 1:

#Input: 1
#Output: "1"
#Explanation: This is the base case.

## time: O(m * n); space: 
def countAndSay(n: int) -> str:
    if n==1:
        return '1'
    def countSay(num_str):
        count=1
        out=''
        for i in range(1, len(num_str)):
            if num_str[i]==num_str[i-1]:
                count+=1
            else: 
                out+=str(count)+num_str[i-1]
                count=1
        out+=str(count)+num_str[-1]
        return out
    out='1'
    for _ in range(n-1):
        out=countSay(out)
    return out


countSay('1211')