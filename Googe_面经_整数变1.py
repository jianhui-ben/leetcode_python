
#给你一个整数，有三种操作：除二，除三，减一，问最少需要多少步能到达1。

def minStep(x):
    
    ## recursion
    ## minStep(x-1)+1, minStep(x/2)+1, minStep(x/3)+1
    ## O(n) time, O(n) space
    ## greedy: time: O(3**N)
    def recursion(x, mem):
        if x==1:
            return 0
        option =set()
        if x%2==0:
            option.add(1+ recursion(x/2,mem))
        if x%3 == 0 :
            option.add(1+recursion(x/3, mem))
        option.add(1+recursion(x-1, mem))
        mem[x] = min(option)
        return mem[x]
    return recursion(x, mem)


x= 18
print(minStep(x))