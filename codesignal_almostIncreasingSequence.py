#Given a sequence of integers as an array, determine whether it is possible to obtain a strictly 
#increasing sequence by removing no more than one element from the array.
#Note: sequence a0, a1, ..., an is considered to be a strictly increasing if a0 < a1 < ... < an.
# Sequence containing only one element is also considered to be strictly increasing.

#Example

#For sequence = [1, 3, 2, 1], the output should be
#almostIncreasingSequence(sequence) = false.

#There is no one element in this array that can be removed in 
#order to get a strictly increasing sequence.

def almostIncreasingSequence(sequence):
    def alwayIncreasing(arr):
        if not arr or len(arr)==1: return True
        for i in range(1, len(arr)):
            if arr[i-1]>= arr[i]:
                return False
        return True
        
    if not sequence or len(sequence)==1: return True
    if alwayIncreasing(sequence[1:]): return True
    for i in range(1, len(sequence)):
        if sequence[i-1]>= sequence[i]:
            return alwayIncreasing(sequence[:i]+ sequence[i+1:]) or alwayIncreasing(sequence[:i-1]+ sequence[i:])
    return True

def almostIncreasingSequence(sequence):
    droppped = False
    last = prev = min(sequence) - 1
    for elm in sequence:
        if elm <= last:
            if droppped:
                return False
            else:
                droppped = True
            if elm <= prev:
                prev = last
            elif elm >= prev:
                prev = last = elm
        else:
            prev, last = last, elm
    return True
