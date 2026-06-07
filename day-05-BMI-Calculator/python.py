weight = float(input("Enter weight:"))
height = float(input("Enter height:"))
bmi = weight/(height*height)
if bmi < 18.5:
    print("you are underweight")
elif bmi < 25:
    print("you are normal")
elif bmi < 30:
    print("you are overweight")
else:
    print("you are obese")

print("Your BMI:",round(bmi,2))
