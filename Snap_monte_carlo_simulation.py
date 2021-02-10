#N个 Turkers标数据，数据很模糊基本靠瞎猜，有M个选项可选。
#问这些人达到了majority共识的概率有多大？也就是有超过半数的人都选了某一选项的概率。

#要求先给出数学解析解，然后给出coding实现方法来求近似解。

#代码其实很简单，Monte Carlo simulation，跑个足够多的次数，用统计结果来近似概率

## p= (1/M)**(N//2)

print(12//2)


import random
random.randint(1, 2)


import collections
collections.Counter([1,1,1,2, 3,3,3,3]).most_common(1)[0][1]

def prob(M, N):
    import random
    import collections
    major=0
    for _ in range(100000):
        choices= [None]* N
        for i in range(N):
            choices[i]= random.randint(1, M)
        if collections.Counter(choices).most_common(1)[0][1]> int(N//2):
            major+=1
    return float(major)/100000.0*100.0

def verify(M, N):
    return (1.0/float(M))**int(N//2)*100.0

verify(7, 3)
prob(7, 3)