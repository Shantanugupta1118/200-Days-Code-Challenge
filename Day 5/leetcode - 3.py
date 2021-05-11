# Contribution By: Shantanu Gupta
# Github: Shantanugupta1118
# DAY 5 of DAY 100
# Leetcode 3 - Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/



# Solution:  -- 

def main():
    s = input()
    count = 0
    mx = 0
    st = ''
    j= 0
    while j<len(s):
        i = j
        count = 0
        st = ''
        while i<len(s):
            if s[i] not in st:
                st += s[i]
                count += 1
            else:
                mx = max(mx, count)
                i -= 1
                break
            mx = max(mx, count)
            i += 1
        j += 1
    print(mx)

main()
