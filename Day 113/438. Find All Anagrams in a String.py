# Github: Shantanugupta1118
# DAY 113 of DAY 200
# 438. Find All Anagrams in a String



class Solution:
    '''
    # Partial Accepted
    # TLE error
    
    def solve(self, s, p):
        res = []
        for i in range(len(s)-len(p)+1):
            temp = p
            counter = len(p)
            if s[i] in p:
                for j in range(len(p)):
                    if s[i+j] in temp:
                        temp = temp.replace(s[i+j], "", 1)
                        print(s[i+j], temp)
                        counter -= 1
                    else: break
                if not temp and counter == 0:
                    res.append(i)
        return res
    '''
    
    def solve(self, s, p):
        dic_s, dic_p = [0]*26, [0]*26
        outpt = []
        for letter in p:
            index = ord(letter)-97
            dic_p[index] += 1
        i = 0
        for j in range(len(s)):
            index = ord(s[j])-97
            dic_s[index] += 1
            if j >= len(p)-1:
                if dic_s == dic_p:
                    outpt.append(i)
                dic_s[ord(s[i])-97] -= 1
                i += 1
        return outpt
    
    
print(Solution().solve("cbaebabacd", "abc"))
print(Solution().solve("ababababab","aab"))

