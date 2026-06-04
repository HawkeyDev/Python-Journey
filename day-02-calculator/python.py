print("Select operation:")
print("1. Addition +")
print("2. Subtraction -")
print("3. Multiplication *")
print("4. Division /")
print("5. Square ")
print("6. Exponential")
print("7. Square root")
i = int(input("enter the operation number:"))
x = int(input("enter the first number:"))
if i in [1,2,3,4,6]:
    y = int(input("enter the second number:"))
if i == 1:
    result = x + y
elif i == 2:
    result = x - y
elif i == 3:
    result = x * y
elif i == 4:
    result = x / y
elif i == 5:
    result = x ** 2
elif i == 6:
    result = x ** y
elif i == 7:
    result = x ** 0.5        
else:
    print("Operation unavailable")
    result = None

if result is not None:
    print("Result:", result)
    