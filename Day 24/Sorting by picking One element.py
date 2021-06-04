# Github: Shantanugupta1118
# DAY 23 of DAY 100
# Check if an Array can be Sorted by picking only the corner Array elements - GFG
# https://www.geeksforgeeks.org/check-if-an-array-can-be-sorted-by-picking-only-the-corner-array-elements/



def check_sort(arr):
    flag = False
    for i in range(1, len(arr)):
        if arr[i]-arr[i-1] > 0 and flag:
            return False
        if arr[i] - arr[i-1] < 0:
            flag = True
    return True

arr = [2,5,6,3,1,4,7,9,3]
print(check_sort(arr))
arr = [1,2,3,4,5,6,3,2,1]
print(check_sort(arr))
arr = [5,6,9,10,25,36,20,14,6]
print(check_sort(arr))