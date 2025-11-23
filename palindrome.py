string = input("Enter a string: ")

# Remove spaces and convert to lowercase for accurate checking
s = string.replace(" ", "").lower()

if s == s[::-1]:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
