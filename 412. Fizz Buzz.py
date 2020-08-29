#write a program that outputs the string representation of numbers from 1 to n.

#but for multiples of three it should output “fizz” instead of the number and for the multiples of five output “buzz”. for numbers which are multiples of both three and five output “fizzbuzz”.

#example:

#n = 15,

#return:
#[
#    "1",
#    "2",
#    "fizz",
#    "4",
#    "buzz",
#    "fizz",
#    "7",

class Solution(object):
    def fizzBuzz(self, n):
        """
        
        :type n: int
        :rtype: List[str]
        """
        ##naive method
        """
        l= []
        for i in range(1, n+1):
            if i%3==0 and i%5==0:
                l.append('FizzBuzz')
            elif i%3==0:
                l.append('Fizz')
            elif i%5==0:
                l.append('Buzz')
            else:
                l.append(str(i))
        return l
        """
        ##string concatenation
        l = []

        for num in range(1,n+1):

            divisible_by_3 = (num % 3 == 0)
            divisible_by_5 = (num % 5 == 0)

            num_ans_str = ""

            if divisible_by_3:
                # Divides by 3
                num_ans_str += "Fizz"
            if divisible_by_5:
                # Divides by 5
                num_ans_str += "Buzz"
            if not num_ans_str:
                # Not divisible by 3 or 5
                num_ans_str = str(num)

            # Append the current answer str to the ans list
            l.append(num_ans_str)  

        return l