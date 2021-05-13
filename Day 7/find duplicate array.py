# Contribution By: Shantanu Gupta
# Github: Shantanugupta1118
# DAY 7 of DAY 100
# InterviewBit - Find duplicate in array
# https://www.interviewbit.com/problems/find-duplicate-in-array/


# Solution

def main():
    arr = list(map(int, input().split()))
    d = dict()
    for i in arr:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for i in d:
        if d[i] > 1:
            print(d[i], i)

main()