# 就是每一轮，有且只有一个队伍得分，得分只能是2或5或7，然后这三种分数可以重复使用，问7：5的所有组合方式
# 举例，
# 第一场 A得2分
# 第二场 A得5分
# 第三场 B得5分
# 就是一种7-5的得分方式，问一共有几种方式


out=0
test=[]
def scores():
    global out
    def dfs(a, b, record):
        global out
        global test
        if (a==7 and b==5) or (a==5 and b==7):
            out+=1
            test.append(record)
        elif a>7 or b>7:
            return
        for i in [2,5,7]:
            dfs(a+i, b, record+'a'+str(i))
            dfs(a, b+i, record+'b'+str(i))
    dfs(0, 0, '')
    return out

print(scores())
print(test)
    
    
    
