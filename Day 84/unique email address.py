# Github: Shantanugupta1118
# DAY 84 of DAY 100

class Solution:
    # ------- Full TC Passed - 84ms Runtime ---------------
    """
    def solve(self):
        # arr = list(map(str, input().split()))
        arr = ["test.email+alex@leetcode.com", "test.email@leetcode.com"]
        filter = {}
        for i in range(len(arr)):
            s = ""
            atrate = arr[i].index("@")
            for j in range(len(arr[i])):
                if arr[i][j] != "@":
                    if arr[i][j] != "." and arr[i][j] != "+":
                        s += arr[i][j]
                        # print("N  :", s)
                    elif arr[i][j] == ".":
                        # print(".  :", s)
                        continue

                    elif arr[i][j] == "+":
                        s += arr[i][atrate:]
                        # print("+: ", s)
                        break
                else:
                    s += arr[i][j:]
                    break
            print(s, filter)
            if s in filter:
                filter[s] += 1
            else:
                filter[s] = 1
        return len(filter), filter
        """

# ----------- FUll TC Passed - 48ms Runtime -----------
    def solve(self):
        arr = ["test.email+alex@leetcode.com", "test.email@leetcode.com"]
        def unique_emails(email):
            local, domain = email.split('@')
            local = local.replace(".", "")
            check_plus = local.find("+")
            if check_plus!= -1:
                local = local[:check_plus]
            return local+"@"+domain
        return len({(unique_emails(email)) for email in arr})


print(Solution().solve())