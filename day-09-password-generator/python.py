import string
import random
characters = string.ascii_letters + string.digits + string.punctuation
random.choice(characters)
password = ""
length = int(input("enter password length:"))
for i in range(length):
    password += random.choice(characters)
print(password)