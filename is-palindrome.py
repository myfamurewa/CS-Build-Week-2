import re
palindrome = "A man, a plan, a canal: Panama"
Notpalindrome = "Race a car"
test3 = "I'm a lasagna sang a salami"
test4 = "ab_a"
test5 = "a common trade-off"

def is_Palindrome(s: str) -> bool:
    s = re.sub(r'[\W_]', '', s).lower()
    s2 = s[::-1]
    return s == s2

print(is_Palindrome(palindrome))
print(is_Palindrome(Notpalindrome))
print(is_Palindrome(test3))
print(is_Palindrome(test4))
print(is_Palindrome(test5))

def is_Palindrome_v2(s: str) -> bool:
    i0 = 0
    i1 = len(s) -1

    if s == "":
        return True

    while i1 > i0:
        if not s[i0].isalnum():
            i0 += 1
            continue
        if s[i0].lower() != s[i1].lower():
            return False
        
        i0 += 1
        i1 -= 1
    return True
print("***************************V2**********************")
print(is_Palindrome_v2(palindrome))
print(is_Palindrome_v2(Notpalindrome))
print(is_Palindrome_v2(test3))
print(is_Palindrome_v2(test4))
print(is_Palindrome_v2(test5))

def recursive_palindrome(s: str) -> bool:
    print(s)
    if len(s) <= 1:
        return True
    else:
        return is_Palindrome(s[1:-1])
    # if len(s) < 2:
    #     return True
    # return s[0] == s[-1] and isPalindrome(s[1: -1])
print("*************RECURSIVE*****************")
print(recursive_palindrome(palindrome))
# print(recursive_palindrome(Notpalindrome))
print(recursive_palindrome("abba"))
print(recursive_palindrome("Kayak"))
print(recursive_palindrome(test3))