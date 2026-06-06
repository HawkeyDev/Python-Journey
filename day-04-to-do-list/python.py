import json

try:
    with open ("tasks.json","r") as f:
        tasks = json.load(f)

except:
    tasks={}

while True:
    print ("\n To-Do-List")
    print("select operation:")
    print("1.Add Task")
    print("2.Finish task") 
    print("3.Show all tasks")
    print("4.Exit")   

    choice = int(input("Enter choice: "))

    if choice == 1:
        work = input("Enter Task:")
        tasks[work]="pending"
        with open("tasks.json","w") as f:
            json.dump(tasks,f)
        print("task addded!!")
    elif choice == 2:
        work = input("Enter Task to finish:")
        if work in tasks:
            tasks[work]="done"
            with open("tasks.json","w") as f:
                json.dump(tasks,f)
            print("task completed successfully!!!")
        else:
            print("task not found")
    elif choice == 3:
        if len(tasks) == 0:
            print("No tasks found!")
        else:
            print("\nAll tasks:")
            for work,status in tasks.items():
                print(work, ":",status)
    elif choice == 4:
        print("goodbye!!!") 
        break