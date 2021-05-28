#给一个int array，每个value是三角形的一条边，判断每连续三个value能不能构成一个三角形。三角形判断方法是任意两边的和大于第三边

arr=[2,3,4,5,6, 4, 5]

def checkTriangle(arr):
    i, out=0, []
    
    while i+2<len(arr):
        out.append(arr[i]+arr[i+1]>arr[i+2] and \
                    arr[i+2]+arr[i+1]>arr[i] and \
                    arr[i]+arr[i+2]>arr[i+1])
        i+=1
    return out
