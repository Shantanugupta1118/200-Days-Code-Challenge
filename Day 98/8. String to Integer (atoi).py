# Github: Shantanugupta1118
# DAY 98 of DAY 100
# 8. String to Integer (atoi)

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip() 
        signs = ['-', '+']
        res = ''

        for i, char in enumerate(s):
            if char in signs and i == 0:
                res += char
                continue

            if char.isnumeric():
                res += char
            else:
                break

        if not res or res in signs:
            return 0

        res = max(min(int(res), 2**31 - 1), -2**31)
        return res        

print(Solution().myAtoi())