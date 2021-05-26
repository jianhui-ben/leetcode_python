#1. 判断相邻String首尾相同
#给长度为n的String[] input，判断 input和input[i+1]的首位char相同，返回长度为n-1的boolean[] res。
#举例：input = ["abc", "acc", "bcc"], res = [true, false]

input = ["abc", "acc", "bcc", 'ccd', 'cdb']
#res = [True, False]
def connectOrNot(input):
    out = []
    if len(input)<2: return out
    temp= input
    second=input.pop(0)
    while temp:
        first = second
        second = temp.pop(0)
        out.append(first[0]==second[0])
    return out

print(connectOrNot(input))