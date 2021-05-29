#unique on segment。给一个数组和一个整数k，
#例如arr= [1,2,3,4,2], k=3. 求有多少的subarr可以满足subarr中的数字都是unique的且至少有k个。
#[1,2,3], [1,2,3, 4], [2,3,4], [3,4,2], 一共有4个subarray


arr= [1,3,2,4,3]
k=3


# a arrary with 5 unique nums has 5-k+1 subsequences with k unique characters

def checkAtLeastKuniNumber(arr, k):
    left, right =0, 0
    path=set()
    ans = 0
    while right< len(arr):
        path.add(arr[right])
        right +=1

        ## we shrink the window when arr[right] in path
        while right<len(arr) and arr[right] in path:
            if len(path)>=k: 
                ans+=len(path)-k+1
            path.remove(arr[left])
            left+=1

        ## last run:
    while len(path)>=k:
        ans+=len(path)-k+1
        path.remove(arr[left])
        left+=1        
    return ans
print(checkAtLeastKuniNumber(arr, k))