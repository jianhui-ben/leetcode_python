#88. Merge Sorted Array
#Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

#The number of elements initialized in nums1 and nums2 are m and n respectively.
#You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.
#Example:

#Input:
#nums1 = [1,2,3,0,0,0], m = 3
#nums2 = [2,5,6],       n = 3

#Output: [1,2,2,3,5,6]
 

#Constraints:

#-10^9 <= nums1[i], nums2[i] <= 10^9
#nums1.length == m + n
#nums2.length == n

def merge(nums1, m, nums2, n):
    if m==0:
        nums1[:]=nums2   ## very wierd thing
        return
    if n==0:
        return
    list1=nums1[:m]
    for i in range(len(nums1)-1, -1, -1):
        if list1[m-1]<= nums2[n-1]:
            nums1[i]= nums2[n-1]
            n-=1
            if n==0:
                nums1[:i]= list1[:m]
                return
        else:
            nums1[i]=list1[m-1]
            m-=1
            if m==0:
                nums1[:i]= nums2[:n]
                return
        
#merge(nums1, m, nums2, n)


nums1=[0]
m=0
nums2=[1]
n=1
merge(nums1, m, nums2, n)
nums1

