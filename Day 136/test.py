# Ques 1

# def ss(strParam):
#     n = list(map(str, strParam.split(' ')))[::-1]
#     return " ".join(n)
    
# print(ss("1 2 3"))
# print(ss("10 20 30"))



#  ques 2


def swap_palindrome(strparam):
    def palindrom(s):
        return s == s[::-1]

    if palindrom(strparam):
        return strparam
        
    s = list(strparam)
    for i in range(len(s)-1):
        s[i], s[i+1] = s[i+1], s[i]
        if palindrom(s):
            return "".join(s)
        else:
            s[i], s[i+1] = s[i+1], s[i]
    return "-1"

print(swap_palindrome("anna"))
print(swap_palindrome("kyaak"))
print(swap_palindrome("rcaecar"))
print(swap_palindrome("madam"))