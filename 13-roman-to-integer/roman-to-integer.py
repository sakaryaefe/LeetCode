class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total_num = 0 
        for i in range(len(s) - 1):
            if roman_to_int[s[i]] < roman_to_int[s[i + 1]]:
                total_num = total_num - roman_to_int[s[i]]
            else: 
                total_num = total_num + roman_to_int[s[i]]
        total_num = total_num + roman_to_int[s[-1]]
        return total_num            
        