#187. Repeated DNA Sequences

#All DNA is composed of a series of nucleotides abbreviated as 
#'A', 'C', 'G', and 'T', for example: "ACGAATTCCG". When studying DNA, 
#it is sometimes useful to identify repeated sequences within the DNA.

#Write a function to find all the 10-letter-long sequences (substrings) 
#that occur more than once in a DNA molecule.

 

#Example 1:

#Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
#Output: ["AAAAACCCCC","CCCCCAAAAA"]


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ##brute force
        out=[]
        stored=dict()
        i= 0
        while i+9< len(s):
            if s[i:i+10] in stored and stored[s[i:i+10]]==1:
                out.append(s[i:i+10])
                stored[s[i:i+10]]+=1
            elif s[i:i+10] not in stored :
                stored[s[i:i+10]]=1
            i+=1
        
        return out
            