#A sequence of number is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

#For example, these are arithmetic sequence:

#1, 3, 5, 7, 9
#7, 7, 7, 7
#3, -1, -5, -9
#The following sequence is not arithmetic.

#1, 1, 2, 5, 7

#A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.

#A slice (P, Q) of array A is called arithmetic if the sequence:
#A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.

#The function should return the number of arithmetic slices in the array A.


#Example:

#A = [1, 2, 3, 4]

#return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.

class Solution(object):

        
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        
        #method 1: use formula
        """
        """
        if len(A)< 3:
            return 0
        else:
            num=0
            head= 0
            tail= 1
            
            for i in range(2, len(A)):
                dif= A[tail]-A[tail-1]
                if A[i]-A[i-1]==dif:
                    tail+=1
                else:
                    num+= sum(range(tail-head))
                    head, tail = i-1, i
            num+= sum(range(tail-head))
        return num
        """
        """
        ###method 2: recursive method:
        def slice(A, i, s):
            if i<2:
                return 0
            ap=0
            if (A[i]-A[i-1] == A[i-1] - A[i-2]):
                ap=1+slice(A, i-1)
                s+=ap
                return s
            else:
                return slice(A, i-1, s)

        s=0    
        a=slice(A, len(A)-1, s)
        return a
        """
        
        # method 3: dynamic programming:
        if len(A)< 3:
            return 0
        l=[0]* len(A)
        sum=0
        for i in range(2, len(A)):
            if A[i]-A[i-1]==A[i-1]-A[i-2]:
                l[i]=1+ l[i-1]
                sum+=l[i]
        return sum
  