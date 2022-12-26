class Solution:
    def romanToInt(self, s: str) -> int:
        roman_value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D':500, 'M':1000}
        num = 0
        for i in range(len(s)):
            if i + 1 < len(s) and roman_value[s[i]] < roman_value[s[i + 1]]:
                num -= roman_value[s[i]]
            else:
                num += roman_value[s[i]]
        return num

