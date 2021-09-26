# Github: Shantanugupta1118
# DAY 81 of DAY 100

class Solution:
    # ---------- 7 /88 TC ------------------
    # def solve(self):
    #     mx = -99
    #     arr = list(map(str, input().split()))
    #     # print(arr, len(arr))
    #     if len(arr)==1: return len(arr[0])
    #     for i in range(len(arr)-1):
    #         temp = arr[i]+arr[i+1]
    #         mx = max(mx, len(temp))
    #         # print(temp)
    #     return mx


    # ---------------- 31 / 88 TC ----------
    # def solve(self):
    #     temp = list(map(str, input().split()))
    #     # temp = ["ab","ba","cd","dc","ef","fe","gh","hg","ij","ji","kl","lk","mn","nm","op","po"]
    #     # new_arr_set = []
    #     mx = -9999
    #     arr = []
    #     for i in range(len(temp)):
    #         x = sorted(temp[i])
    #         if x not in arr:
    #             arr.append(x)

    #     # print(arr)
    #     check_set = set()
    #     n = len(arr)
    #     final = ""
    #     for i in range(n):
    #         for j in range(i, n):
    #             for k in range(len(arr[j])):
    #                 if arr[j][k] not in final:
    #                     final += arr[j][k]
    #                     check_set.add(arr[j][k])
    #                     # new_arr_set.append(len(final))
    #                     mx = max(len(final), mx)
    #                     # print(final)
    #                 else:
    #                     # new_arr_set.append(final)
    #                     final = ""
    #     # return final
    #     return mx


    # ---------- FULL TC PASSED - 99.52% runtime beat | 28ms Runtime --------------
    def solve(self, arr):
        prev_rec = {0 : 0}
        for i in arr:
            if len(i) == len(set(i)):
                maske_value = sum([1<<(ord(c)-97) for c in i])
                prev_rec.update({res+maske_value : prev_rec[res]+len(i) for res in prev_rec if not maske_value&res})
        return max(prev_rec.values())





for _ in range(int(input())):
    arr = list(map(str, input().split()))
    print(Solution().solve(arr))