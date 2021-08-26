#537. Complex Number Multiplication
#A complex number can be represented as a string on the form "real+imaginaryi" where:

#real is the real part and is an integer in the range [-100, 100].
#imaginary is the imaginary part and is an integer in the range [-100, 100].
#i2 == -1.
#Given two complex numbers num1 and num2 as strings, return a string of the complex number that represents their multiplications.

 

#Example 1:

#Input: num1 = "1+1i", num2 = "1+1i"
#Output: "0+2i"
#Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        """
        math: 
        (a1 *a2 -b1 *b2) + (a2*b1 +a1*b2) I
        
        """
        a1, b1 = int(num1[:num1.index('+')]), int(num1[num1.index('+') + 1: num1.index('i')])
        a2, b2 = int(num2[:num2.index('+')]), int(num2[num2.index('+') + 1: num2.index('i')])
        return str(a1 * a2 - b1 * b2) + '+' + str(a2 * b1 + a1 * b2) + 'i'
