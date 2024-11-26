class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        total = 0 #initialize total to zero to add and subtract from that  
        length = len(s)
        for i in range(length):
            if i < length -1 and roman[s[i]] < roman[s[i+1]]: # this it means when the value is not last in character and the current value is less than from the next it will follows the substraction rules 
                total -= roman[s[i]]
            else:
                total += roman[s[i]]
        return total
