# Github: Shantanugupta1118
# DAY 71 of DAY 100
# 598. Range Addition II - Leetcode/August



class solution:
    def maxCount(self, m, n, ops):
        if len(ops)==0:
            return m*n
        x, y = [], []
        for query in ops:
            x.append(query[0])
            y.append(query[1])
        row, col = min(x), min(y)
        return row*col

print(solution().maxCount(m = 26, n = 17, ops = [[20,10],[26,11],[2,11],[4,16],[2,3],[23,13],[7,15],[11,11],[25,13],[11,13],[13,11],[13,16],[26,17]]))