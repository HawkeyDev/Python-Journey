print("\n Temperature Convertor")
print("1.Celsius to Fahrenheit")
print("2.Fahrenheit to Celsius")
print("3.Celsius to Kelvin")
choice = int(input("Enter choice: "))
if choice == 1:
    temp = float(input("Enter Celsius: "))
    result = (temp * 9/5) + 32
    print("Fahrenheit:", round(result, 2))
elif choice == 2:
    temp = float(input("Enter Fahrenheit: "))
    result = (temp - 32) * 5/9
    print("Celsius:", round(result, 2))
elif choice == 3:
    temp = float(input("Enter Celsius: "))
    result = temp + 273.15
    print("Kelvin:", round(result, 2))
else:
    print("invalid input")
