
#Write a function to find the longest common prefix string amongst an array of strings.

#If there is no common prefix, return an empty string "".

#Example 1:

#Input: ["flower","flow","flight"]
#Output: "fl"
#Example 2:

#Input: ["dog","racecar","car"]
#Output: ""
#Explanation: There is no common prefix among the input strings.

## typical method (horizontal scanning)
def longestCommonPrefix(strs):
    def prefix_between_two(str1, str2):
        prefix= ''
        if len(str1)!=0 and len(str2)!=0:
            for i in range(0, min(len(str1), len(str2))):
                if str1[i]==str2[i]:
                    prefix+=str1[i]
                else:
                    return prefix
        return prefix
    if len(strs)==1:
        return strs[0]
    elif len(strs)==0:
        return ''
    out= strs[0]
    for i in range(1, len(strs)):
        out= prefix_between_two(out, strs[i])
    return out


##common prefix:
def prefix_between_two(str1, str2):
    prefix= ''
    if len(str1)!=0 and len(str2)!=0:
        for i in range(0, min(len(str1), len(str2))):
            if str1[i]==str2[i]:
                prefix+=str1[i]
            else:
                return prefix
    return prefix

## common continuous substring
def common_between_two(str1, str2):
    if len(str1)!=0 and len(str2)!=0:
        #head, tail= str1, str1
        head= str1
        while len(head)!=0:
            if str2.find(head)!=-1:
                return head
            #if str2.find(tail)!=-1:
            #    return tail
            head= head[0:len(head)-1]
            #tail= tail[1:len(tail)]
    return ''

##test cases
a='abc'
b='bcd'
common_between_two('c','ac')

longestCommonPrefix(['cb','b'])