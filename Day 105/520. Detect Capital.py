# Github ID: Shantanugupta1118
# Day 105 of Day 200
# 520. Detect Capital


class Solution:
    def detectCapital(self, word):
        if word.isupper() or word.islower() or word.istitle():
            return True
        return False


print(Solution().detectCapital("leetcode"))
print(Solution().detectCapital("Leetcode"))
print(Solution().detectCapital("LeeTcode"))
print(Solution().detectCapital("LEETCODE"))
