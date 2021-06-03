#input: abababababac , {ab, abab, abc}问对应的String在大字符里出现了几次，
#不考虑重叠情况，  output {4, 2, 0}
s = 'cabababababac'
print(s[1:3]=='ab')
l=['ab', 'abab', 'abc', 'bac']
def countSet(s, l):
    res=[]
    def countMatch(s, t):
        if not s or not t or len(s)<len(t):
            return 0
        left, right = 0, 0
        out = 0
        while right<len(s):
            right+=1
            if s[left:right]==t:
                out+=1
                left = right
            while right-left>=len(t):
                left+=1
        return out

    for i in l:
        res.append(countMatch(s, i))
    return res
    
print(countSet(s, l))