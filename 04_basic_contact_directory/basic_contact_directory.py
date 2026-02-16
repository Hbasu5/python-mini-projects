# Contact Directory
contacts = {}
print("\n1. Add Contact")
print("2. View Contacts")
print("3. Search Contact")
print("4. Exit")
while True:
    try:
        ch = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Enter a number 1-4.")
        continue
    if ch == 1:
        name = input("Enter name: ")
        label = input("Enter label (Home/Office/Mobile): ")
        number = input("Enter number: ")
        if name not in contacts:
            contacts[name] = {}
        contacts[name][label] = number
        print("Contact added/updated successfully.")
    elif ch == 2:
        print("Contact Directory:")
        if contacts:
            for person, details in contacts.items():
                print(person)
                for label, number in details.items():
                    print("  ", label, ":", number)
        else:
            print("No contacts saved.")
    elif ch == 3:
        s = input("Enter the name to search: ")
        if s in contacts:
            print("Contact found:")
            for label, number in contacts[s].items():
                print(label, ":", number)
        else:
            print("Contact not found.")
    elif ch == 4:
        print("Exiting...")
        break
    else:
        print("Wrong choice. Try again.")