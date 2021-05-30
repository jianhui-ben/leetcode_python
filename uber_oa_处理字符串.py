#地里有过的面经， 就是给一个字符串string，里面只有 "W" "D" "L" 需要按照以下顺序排列
#1） 如果string 有“W”, 加到result 里， 输入的string remove这个“W” (每次只能remove一个)
#2） 如果string 有“D”, 加到result 里， 输入的string remove这个“D” (每次只能remove一个)
#3） 如果string 有“L”, 加到result 里， 输入的string remove这个“L” (每次只能remove一个)
#4)   如果输入字符串没有 "W" "D" "L" ， return result 不然从step 1重复
#   example: "LDWDL"  -> 输出 "WDLDL"

s = 'LDWDL'
def process(s):
    ## ordered dictionary
    import collections
    temp = {'W':0, 'D':0, 'L':0}
    for i in s:
        temp[i]+=1
    ## use a deque
    stored = collections.deque()
    for i, v in temp.items():
        if v>0:
            stored.append((i, v))
    res=''
    while stored:
        cur_let, v = stored.popleft()
        if v==0:
            continue
        res+=cur_let
        stored.append((cur_let, v-1))
    return res
print(process(s))
    
        
