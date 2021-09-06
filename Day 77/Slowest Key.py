# Github: Shantanugupta1118
# DAY 77 of DAY 100

class Solution:
    def solve(self, time, keyPress):
        times = {time[0]: [keyPress[0]]}
        for i in range(1 , len(time)):
            t = time[i] - time[i - 1]
            if(t in times):
                times[t].append(keyPress[i])
            else:
                times[t] = [keyPress[i]]
        keys = times[max(times.keys())]
        return max(keys)
        # diff = time[0]
        # idx = 0
        # for i in range(1, len(time)):
        #     if time[i]-time[i-1] >= diff:
        #         diff = time[i]-time[i-1]
        #         idx = i
        # # print(diff, keyPress[idx])
        # return keyPress[idx]


release_time = [int(x) for x in input().split()]
keysPressed = input()
print(Solution().solve(release_time, keysPressed))