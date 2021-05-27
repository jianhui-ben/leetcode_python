#题判断给的array是不是逐一递增或递减的rotated array
#比如说 4 5 6 7 1 2 3  -> True
#4 5 6 8 1 2 3  -> False
#4 3 2 1 7 6 5  -> True

##arr=[4,5, 6, 7, 1, 2, 3]
##arr=[4,5, 6, 7, 1, 2, 3]
arr = [4,5, 6, 7, 2, 3]

def consecutiveRotatedArr(arr):
    def check(arr):
        if len(arr)<2: return True
        i, cnt, n = 0, 0, max(arr)
        while i+1<len(arr):
            if arr[i+1]%n - arr[i]%n!=1:
                cnt+=1
            if cnt>1:
                return False
            i+=1
        return True

    return check(arr) or check(arr[::-1])
print(consecutiveRotatedArr(arr))
print(consecutiveRotatedArr(arr))
