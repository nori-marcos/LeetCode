s = "race a car"

palindrome = ""

for char in s:
    if char.isalnum():
        palindrome += char.lower()

reversed_palindrome = palindrome[::-1]

if palindrome == reversed_palindrome:
    print(True)
else:
    print(False)
