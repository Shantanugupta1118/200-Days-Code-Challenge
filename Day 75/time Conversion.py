# Github: Shantanugupta1118
# DAY 75 of DAY 100
# Time Conversion - Hackerrank


import time

def time_convert(s):
    return time.strftime('%H:%M:%S', time.strptime(s, '%I:%M:%S%p'))


s = input()
print(time_convert(s))