# Github: Shantanugupta1118
# DAY 37 of DAY 100
# Paranthese Generate - Leetcode/June 21
# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/605/week-3-june-15th-june-21st/3781/



class solution:
    def generate_paranthesis(self, n):
        res = []
        def solve(string, open_bracket, close_bracket):
            if open_bracket == close_bracket and close_bracket == 0:
                res.append(string)
                return
            if open_bracket:
                solve(string+"(", open_bracket-1, close_bracket)
            if close_bracket > open_bracket:
                solve(string+")", open_bracket, close_bracket-1)
        solve("", n, n)
        return res 

print(solution().generate_paranthesis(4))
print(solution().generate_paranthesis(2))
print(solution().generate_paranthesis(3))