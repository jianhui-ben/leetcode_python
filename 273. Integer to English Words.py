#273. Integer to English Words
#Convert a non-negative integer num to its English words representation.

 

#Example 1:

#Input: num = 123
#Output: "One Hundred Twenty Three"
#Example 2:

#Input: num = 12345
#Output: "Twelve Thousand Three Hundred Forty Five"


class Solution:
    def numberToWords(self, num: int) -> str:
        """
        thousand: 10^3
        million: 10^6
        billion: 10^9
        --trillion: 10 ^ 12
        --quadrillion: 10^15
        123,456
        123 thousand + 456
        """
        if num == 0: return 'Zero'
        
        ## only consider number from 1 to 999
        sigle_digit = {1: 'One', 2: 'Two', 3: 'Three', 4:'Four',\
                       5: 'Five', 6: 'Six',7: 'Seven', 8: 'Eight',9: 'Nine'}
        less_20 = {10: 'Ten', 11:'Eleven', 12:'Twelve', 13: 'Thirteen', \
                   14:'Fourteen', 15: 'Fifteen', 16:'Sixteen', 17: 'Seventeen',\
                   18: 'Eighteen',19:'Nineteen'}
        less_100 = {20: 'Twenty', 30:'Thirty', 40:'Forty', 50:'Fifty', 60:'Sixty', 70:'Seventy', 80:'Eighty', 90:'Ninety'}
        res = ""
        
#         if 1 <= num <= 999:
#             hundred = num // 100
#             rest = num % 100
#             if hundred:
#                 res = res + sigle_digit[hundred] + ' Hundred'
            
#             if rest > 19:
#                 tens = rest // 10 * 10
#                 rest_digit = rest - tens
#                 res = res + less_100[tens]
#                 if rest_digit:
#                     res = res + sigle_digit[rest_digit]
#             elif rest > 9:
#                 res = res + less_20[rest]
#             elif rest <= 9:
#                 res = res + sigle_digit[rest]
                
        
        billion = num // (10**9)
        million = (num - billion * (10**9)) // (10**6)
        thousand = (num - billion * (10**9) - million * (10**6)) // (10**3)
        rest = num - billion * (10**9) - million * (10**6) - thousand * (10**3)
        
        
        if billion:
            if res: res = res + ' '
            res = res + self.numberToWords(billion) + ' Billion'
        
        if million:
            if res: res = res + ' '
            res = res + self.numberToWords(million) + ' Million'
        
        if thousand:
            if res: res = res + ' '
            res = res + self.numberToWords(thousand) + ' Thousand'       
        
        if rest:
            num = rest
            
            hundred = num // 100
            rest = num % 100
            if res: res = res + ' '
            if hundred and rest:
                res = res + sigle_digit[hundred] + ' Hundred '
            elif hundred:
                res = res + sigle_digit[hundred] + ' Hundred'
                
            if rest > 19:
                tens = rest // 10 * 10
                rest_digit = rest - tens
                res = res + less_100[tens]
                if rest_digit:
                    if tens: res = res + ' '
                    res = res + sigle_digit[rest_digit]
            elif rest > 9:
                res = res + less_20[rest]
            elif 0< rest <= 9:
                res = res + sigle_digit[rest]
        return res