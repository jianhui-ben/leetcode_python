#833. Find And Replace in String
#To some string S, we will perform some replacement operations that replace groups of letters with new ones (not necessarily the same size).

#Each replacement operation has 3 parameters: a starting index i, a source word x and a target word y.  The rule is that if x starts at position i in the original string S, then we will replace that occurrence of x with y.  If not, we do nothing.
class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        ## hashtable
        ## followup: 
        stored= defaultdict()
        for i in range(len(indexes)):
            stored[indexes[i]]= (sources[i], targets[i])
        
        stored = {k:v for k, v in sorted(stored.items())}
        out = ''
        k=0
        while k<len(S):
            if k not in stored:
                out+=S[k]
                k+=1
            else:
                src, tar = stored[k]
                if len(S[k:])>=len(src) and S[k: k+len(src)]==src:
                    out+=tar
                    k+= len(src)
                else:
                    out+=S[k]
                    k+=1
        return out
        