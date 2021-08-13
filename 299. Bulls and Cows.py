#299. Bulls and Cows
#You are playing the Bulls and Cows game with your friend.

#You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:

#The number of "bulls", which are digits in the guess that are in the correct position.
#The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
#Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

#The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.

 

#Example 1:

#Input: secret = "1807", guess = "7810"
#Output: "1A3B"
#Explanation: Bulls are connected with a '|' and cows are underlined:
#"1807"
#  |
#"7810"
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        """
        xAyB:
        x: how many digits are in right positions
        y: how many can be re arranged
        """
        counter =  defaultdict(int)
        x, y = 0, 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                x += 1
            else:
                s, g = secret[i], guess[i]
                if counter[s] < 0: y += 1
                if counter[g] > 0: y += 1
                counter[s] += 1
                counter[g] -= 1
        
        return str(x) + 'A' + str(y) + 'B'
        