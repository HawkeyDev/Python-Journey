i = int(input("Enter a number to generate Fibonacci sequence: "))
a = 0
b = 1
for x in range(i):
    print(a)
    a, b = b, a + b