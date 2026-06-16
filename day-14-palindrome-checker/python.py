i = input("Enter a string to check if it is a palindrome: ")
if i == i[::-1]:
    print(f"{i} is a palindrome.")
else:
    print(f"{i} is not a palindrome.")