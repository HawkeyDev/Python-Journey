import time
sec = int(input("Enter the number of seconds for the countdown timer: "))
for i in range(sec, -1, -1):
    print(i)
    time.sleep(1)
else:
    print("Time's up!")