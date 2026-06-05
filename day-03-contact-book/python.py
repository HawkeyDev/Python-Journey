import json

# 1. Load first
try:
    with open("contacts.json", "r") as f:
        contacts = json.load(f)
except:
    contacts = {}

while True:
    print("\nContact Book")
    print("1. Add contact")
    print("2. Delete contact")
    print("3. Search contact")
    print("4. View all contacts")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        with open("contacts.json", "w") as f:
            json.dump(contacts, f)
        print("Contact saved!")

    elif choice == 2:
        user = input("Enter name to delete: ")
        if user in contacts:
            contacts.pop(user)
            with open("contacts.json", "w") as f:
                json.dump(contacts, f)
            print("Contact deleted!")
        else:
            print("Contact not found!")

    elif choice == 3:
        user = input("Enter name: ")
        if user in contacts:
            print("Name:", user)
            print("Phone:", contacts[user])
        else:
            print("Contact not found!")

    elif choice == 4:
        if len(contacts) == 0:
            print("No contacts found!")
        else:
            print("\nAll Contacts:")
            for name, phone in contacts.items():
                print(name, ":", phone)

    elif choice == 5:
        print("Goodbye!")
        break