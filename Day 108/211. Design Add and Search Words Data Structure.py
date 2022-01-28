# Github: Shantanugupta1118
# DAY 109 of DAY 100
# 211. Design Add and Search Words Data Structure


import re

'''
#   Partial Accepted 
class Solution:
    def __init__(self):
        self.words = []
    
    def addWord(self, word) -> None:
        self.words.append(word)
        
    def search(self, word) -> bool:
        if '.' in word:
            res = re.findall(word, " ".join(self.words))
            for i in res:
                i = i.strip()
                if len(i) == len(word):
                    return True
            return False
        
        else:
            if word in self.words:
                return True
            return False
'''


class Solution:
    def __init__(self):
        self.words = " "
    
    def addWord(self, word) ->None:
        self.words += word + " "
        
    def search(self, word) -> bool:
        return bool(re.search(" {}".format(word.replace('.',"[a-z]")), self.words))
    
wordDic = Solution()
wordDic.addWord("a")
wordDic.addWord("a")
print(wordDic.search("."))
print(wordDic.search("a"))
print(wordDic.search("aa"))
print(wordDic.search("a"))
print(wordDic.search(".a"))
print(wordDic.search("a."))
