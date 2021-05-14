#链接：https://www.nowcoder.com/questionTerminal/14c0359fb77a48319f0122ec175c9ada
#来源：牛客网

#有三种葡萄，每种分别有a,b,c 颗。有三个人，第一个人只吃第1， 2种葡萄，第二个人只吃第2，3种葡萄，第三个人只吃第1， 3种葡萄。
#适当安排三个人使得吃完所有的葡萄,并且且三个人中吃的最多的那个人吃得尽量少。


def eat_grape(a,b,c):
    l= sorted([a,b,c])
    if (l[2]+1)//2>= l[1]+l[0]:
        return (l[2]+1)//2
    return (sum(l)+2)//3
