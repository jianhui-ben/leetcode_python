
#Determine whether an integer is a palindrome. An integer
# is a palindrome when it reads the same backward as forward.

#Example 1:

#Input: 121
#Output: true

#Example 2:

#Input: -121
#Output: false
#Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

##solve it without converting int to string
def isPalindrome(x):
    if x<0:
        return False
    if x<10:
        return True
    first_half, second_half= x, 0
    while first_half>second_half:
        second_half=second_half*10+first_half%10
        if second_half==0:
            return False
        first_half=first_half//10
    if first_half==second_half or (second_half//10==first_half and first_half!=0):
        return True
    return False



##edge case:
isPalindrome(1)
isPalindrome(10)
isPalindrome(21120)