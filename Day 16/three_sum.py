# Github: Shantanugupta1118
# DAY 16 of DAY 100
# 3SUMS - Interviewbits/Leetcode


def main():
    nums = list(map(int, input().split()))
    res = []
    n = len(nums)-1
    nums.sort()                            
    for i in range(n-1):
        if i > 0 and nums[i] == nums[i-1]:  continue
        j, k = i+1, n
        while j < k:
            temp = nums[i] + nums[j] + nums[k]
            if not temp:
                res.append([nums[i], nums[j], nums[k]])
                while j < k and nums[j] == nums[j+1]:
                    j += 1
                    print(nums[j], nums[j+1])
                while j < k and nums[k] == nums[k-1]:
                    k -= 1
                    print(nums[k], nums[k-1])
                print(nums[i], nums[j], nums[k])
                j += 1
                k -= 1
            elif temp < 0:
                j += 1
            else:
                k -= 1
    print(res)




main()
