def is_palindrome(s):
    return s == s[::-1]
w = input("sis")
if is_palindrome(w):
    print("回文です")
else:
    print("回文でない")