import json
import os

def show_menu():
    print("-----------------------------")
    print("       CONTACT BOOK")
    print("-----------------------------")
    print("1. Add contact")
    print("2. View all contacts")
    print("3. Search contact")
    print("4. Delete contact")
    print("5. Update contact")
    print("0. Exit")
    print("-----------------------------")

def save_contacts(contacts):
    with open('contacts.json', "w") as f:
        json.dump(contacts, f, indent=2)
    print("[contacts saved]")

def load_contacts():
    if not os.path.exists("contacts.json"):
        return[]
    with open('contacts.json', 'r') as f:
        return json.load(f)
    
def add_contact(contacts):
    print("-----------------------------")
    name = input('Enter name : ')
    phone = input('Enter phone : ')
    email = input('Enter email :')

    contact = {
        'name' : name,
        "phone" : phone,
        "email": email,
    }

    contacts.append(contact)
    save_contacts(contacts)
    print(f"{name} added successfully!")
    
def view_contacts(contacts):
    print("-----------------------------")
    if len(contacts) == 0:
        print("No contacts yet!")
        return

    for contact in contacts:
        print(f"Name: {contact['name']} Phone: {contact['phone']}")
        print()

def search_contact(contacts):
    print("-----------------------------")
    query = input("Search by name or phone: ").lower()
    results = [c for c in contacts if query in c["name"].lower() 
               or query in c["phone"]]

    if len(results) == 0:
        print("No contacts found!")
        return

    for contact in results:
        print(f"Name  : {contact['name']}")
        print(f"Phone : {contact['phone']}")
        print(f"Email : {contact['email']}")
        print()

def delete_contact(contacts):
    print("-----------------------------")

    view_contacts(contacts)

    if len(contacts) == 0:
        return
    
    try:
        index = int(input("Enter index to delete : "))
        removed = contacts.pop(index)
        save_contacts(contacts)
        print(f"{removed['name']} deleted!")
    except (ValueError, IndexError):
        print('Invalid index!')
        
def update_contact(contacts):
    print("-----------------------------")

    view_contacts(contacts)

    if len(contacts) == 0:
        return
    
    try: 
        index = int(input('Enter index to update :'))
        contact = contacts[index]
        print(f"Available keys: {list(contact.keys())}")

        key = input('Enter key  to update : ')

        if key not in contact:
            print(f"'{key}' is not a valid key!")
            return
        
        value= input('Enter updated value :')
        contacts[index][key] = value
        save_contacts(contacts)
        view_contacts(contacts)
    except (ValueError , IndexError):
        print('Invalid index! ')


def main():
    contacts = load_contacts()

    while True:
        show_menu()
        choice = input('Choose an option: ')
        if choice == '1':
            print('You chose Add contact')
            add_contact(contacts)
        elif choice == "2":
            print("You chose View All contacts")
            view_contacts(contacts)
        elif choice == "3":
            print("You chose Search contact")
            search_contact(contacts)
        elif choice == "4":
            print("You chose Delete contact")
            delete_contact(contacts)
        elif choice == "5":
            update_contact(contacts)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again")

main()

