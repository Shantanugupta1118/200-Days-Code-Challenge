# Contribution By: Shantanu Gupta
# Github: Shantanugupta1118
# DAY 3 of DAY 100

# Problem Statement
'''
    Question: Triplets

    Given 2 numbers N and M and an array of size N.
    A triplets is defined if ti satifies any one of the following conditions.
        * All numbers in triplets are the same. (Eg. (1, 1, 1))
        * The numbers are consecutive (Eg. (1, 2, 3))
    Given the array find the maximum number of triplts that can be formed. All elements of the array are <= M.
    Each element of the array can be part of 1 triplet.


    Input Format: 1 <= N <= 10^5
                  1 <= M <= 10^4
                  1 == arr[i] == M
    Sample:
    TC 1.        4    //N                       |   Output: 1
                 2    //M                       |
                 [1,2,2,2]         //arr[i]     |

    TC 2.       10                              |   Output: 3
                3                               |
                [1,2,2,1,2,1,1,2,1,1]           |

    TC 3.       50                              |   output: 16
                6                               |
                [4,5,1,4,5,2,2,6,4,3,           |
                6,3,2,2,6,4,3,3,4,2,            |
                6,6,6,2,4,5,6,2,4,1,2,          |
                6,3,5,6,1,2,3,5,2,6,            |
                5,2,5,4,2,1,4,5,4]              |
'''


# Solution

def solution_occ(n,m):
    count = 0

    for key in arr_d:
        if arr_d[key] >= 3:
            if arr_d[key]%3==0:
                count += arr_d[key]//3
                arr_d[key] = 0
            else:
                total_occ = arr_d[key]
                extra = 0
                while not total_occ%3==0:
                    total_occ -= 1
                    extra += 1
                count += total_occ//3
                arr_d[key] -= total_occ
    return count

def solution_cons(n, m, s):
    count = 0
    for i in range(len(s)-2):
        if s[i+1]-s[i]==1 and s[i+2]-s[i+1]==1:
            if arr_d[s[i]]>=1 and arr_d[s[i+1]]>=1 and arr_d[s[i+2]]>=1:
                count += 1
                arr_d[s[i]] -= 1
                arr_d[s[i+1]] -= 1
                arr_d[s[i+2]] -= 1
    return count


    

arr_d = dict()
def main():
    # n = int(input())
    # m = int(input())
    # arr = [int(x) for x in input().split()]
    arr = [4,5,1,4,5,2,2,6,4,3,6,3,2,2,6,4,3,3,4,2,6,6,6,2,4,5,6,2,4,1,2,6,3,5,6,1,2,3,5,2,6,5,2,5,4,2,1,4,5,4]
    s = list(set(arr))
    arr.sort()
    for i in arr:
        if i in arr_d: arr_d[i] += 1
        else: arr_d[i] = 1
    res = solution_occ(50, 6) + solution_cons(50, 6, s) 
    print(res)
    # print(solution(n, m, arr))

main()