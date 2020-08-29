#given an array arr of integers, check if there exists two integers n and m such that n is the double of m ( i.e. n = 2 * m).

#more formally check if there exists two indices i and j such that :

#i != j
#0 <= i, j < arr.length
#arr[i] == 2 * arr[j]
 

#example 1:

#input: arr = [10,2,5,3]
#output: true
#explanation: n = 10 is the double of m = 5,that is, 10 = 2 * 5.
#example 2:

#input: arr = [7,1,14,11]
#output: true
#explanation: n = 14 is the double of m = 7,that is, 14 = 2 * 7.
#example 3:

#input: arr = [3,1,7,11]
#output: false
#explanation: in this case does not exist n and m, such that n = 2 * m.

class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if arr.count(0)>1:
            return True
        for i in arr:
            if i!=0 and 2*i in range(min(arr), max(arr)+1):
                if 2*i in arr:
                    return True
        return False
    