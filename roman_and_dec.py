class RomanNumerals:

    def to_roman(self, nums, string=''):
        if nums == 0: return string
        if nums >= 1000: return self.to_roman(nums - 1000, string + 'M')
        if nums >= 900: return self.to_roman(nums - 900, string + 'CM')
        if nums >= 500: return self.to_roman(nums - 500, string + 'D')
        if nums >= 400: return self.to_roman(nums - 400, string + 'CD')
        if nums >= 100: return self.to_roman(nums - 100, string + 'C')
        if nums >= 90: return self.to_roman(nums - 90, string + 'XC')
        if nums >= 50: return self.to_roman(nums - 50, string + 'L')
        if nums >= 40: return self.to_roman(nums - 40, string + 'XL')
        if nums >= 10: return self.to_roman(nums - 10, string + 'X')
        if nums >= 9: return self.to_roman(nums - 9, string + 'IX')
        if nums >= 5: return self.to_roman(nums - 5, string + 'V')
        if nums >= 4: return self.to_roman(nums - 4, string + 'IV')
        if nums >= 1: return self.to_roman(nums - 1, string + 'I')
        

    def from_roman(self, roman_num):
        romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        dec = 0
        for ind in range(len(roman_num)):
            if ind + 1 < len(roman_num) and romans[roman_num[ind]] < romans[roman_num[ind+1]]:
                dec -= romans[roman_num[ind]]
            else:
                dec += romans[roman_num[ind]]
        return dec

numbers = RomanNumerals()
print(numbers.to_roman(44466))