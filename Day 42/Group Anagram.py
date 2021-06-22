# Github: Shantanugupta1118
# DAY 42 of DAY 100
# 49. Group Anagrams - Leetcode
# https://leetcode.com/problems/group-anagrams/



class Solution:
    def groupAnagrams(self, strs):
        anagram = dict()
        for s in strs:
            sorted_str = ''.join(sorted(s))
            if sorted_str in anagram.keys():
                anagram[sorted_str].append(s)
            else:
                anagram[sorted_str] = [s]
        return (anagram.values())


strs = ["eat","tea","tan","ate","nat","bat"]
print(*Solution().groupAnagrams(strs))