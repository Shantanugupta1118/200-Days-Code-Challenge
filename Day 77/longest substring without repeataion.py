# Github: Shantanugupta1118
# DAY 77 of DAY 100

class Solution:
    def solve(self, s):
        characters = set()
        left = right = ans = 0
        length = len(s)

        while right < length:
            if s[right] in characters:
                characters.remove(s[left])
                left += 1
            else:
                characters.add(s[right])
                right += 1
                ans = max(ans, right - left)
        return ans

s = input()
print(Solution().solve(s))