#交错拼接字符串

a='forgeeks'
b = 'forgeeks'
#out= 'adbecfg'


def mergeStr(a,b):
    out =''
    for i in range(min(len(a), len(b))):
        out+= a[i]
        out+= b[i]

    if len(a)>i+1:
        out+=a[i+1:]
    if len(b)>i+1:
        out+=b[i+1:]   
    return out

print(mergeStr(a,b))
