## 1000 coins, 999 fair and 1 double headed. You pick a coin a toss it 10 times,
## all heads, ask what is the probability of this coin being tossed as head in the next time


#P(next head | 10 heads before)=

# P(next head ^ 10 heads before)/ P(10 heads before)
# (P(next head ^ 10 heads before ^ it's fair coin ) + P(next head ^ 10 heads before ^ it's unfair))
# / (P(10 heads before ^ fair) + P(10 heads before ^ unfair))
# = (P(11 heads ^ fair) + P(11 heads ^ unfair) )
# / (P(10 heads ^ fair) + P(10 heads ^ unfair) )
#= ((0.5**11* 999/1000)+ (1/1000))
# / ((0.5**10* 999/1000)+ (1/1000))
print(((0.5**11* 999/1000)+ (1/1000))/ ((0.5**10* 999/1000)+ (1/1000)))







#100个post 0.04概率出广告， 连续 ads个数的期望
#P(is_ads)= 0.04

#P(2 or more ads together)=1- P(next one is not an ads | one ads)
#= 1-(next one is not an ads ^ one ads) / P(one ads)
#= 1- (0.04* 0.96)/ 0.04
#= 

#print(1- (0.04* 0.96)/ 0.04)