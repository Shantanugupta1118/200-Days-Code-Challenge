# Github: Shantanugupta1118
# Day 133 of day 200
# 1491. Average Salary Excluding the Minimum and Maximum Salary



class Solution:
    def avg(self, salary):
        minn, maxx = min(salary), max(salary)
        s = sum(salary)-minn-maxx
        s /= (len(salary)-2)
        return s

print(Solution().avg([4000,3000,1000,2000]))
print(Solution().avg([48000,59000,99000,13000,78000,45000,31000,17000,39000,37000,93000,77000,33000,28000,4000,54000,67000,6000,1000,11000]))