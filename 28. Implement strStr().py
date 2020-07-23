#Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

#Example 1:

#Input: haystack = "hello", needle = "ll"
#Output: 2
#Example 2:

#Input: haystack = "aaaaa", needle = "bba"
#Output: -1

def strStr(haystack: str, needle: str) -> int:
    if needle=='':
        return 0
    return haystack.find(needle)
