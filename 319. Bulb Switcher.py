#319. Bulb Switcher
#There are n bulbs that are initially off. You first turn on all the bulbs, then you turn off every second bulb.

#On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the ith round, you toggle every i bulb. For the nth round, you only toggle the last bulb.

#Return the number of bulbs that are on after n rounds.


class Solution:
    def bulbSwitch(self, n: int) -> int:
        
        """
        5 bulbs
        
        0  0  0  0  0   0
        1  1  1  1  1   5
        1  0  1  0  1   3
        1  0  0  0  1   2
        1  0  0  1  1   3
        1  0  0  1  0   2
        
        18th bulb: 1, 2, 3, 6, 9, 18 
        (1, 18), (2, 9), (3, 6)  --> off
        
        9: 1, 3, 9 --> on
        
        
        
        """
        return int(n**0.5)
