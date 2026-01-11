# Contact Management System using Nested Dictionary

contacts = {}  # Stores contact data: {name: {"phone":..., "email":...}}

def add_contact():
    while True:
        name = input("Enter contact name (or 'q' to quit adding): ").strip()
        if name.lower() == 'q':
            break
        phone = input("Enter phone number: ").strip()
        email = input("Enter email: ").strip()
        if name in contacts:
            print(f"Contact '{name}' already exists. Updating info.")
        contacts[name] = {"phone": phone, "email": email}
        print(f"Contact '{name}' added successfully.\n")

def remove_contact():
    while True:
        name = input("Enter contact name to remove (or 'q' to stop removing): ").strip()
        if name.lower() == 'q':
            break
        if not contacts:
            print("No contacts available to remove.")
            break
        if name in contacts:
            del contacts[name]
            print(f"Contact '{name}' removed successfully.\n")
        else:
            print(f"Error: Contact '{name}' not found.\n")

def search_contact():
    while True:
        name = input("Enter contact name to search (or 'q' to stop searching): ").strip()
        if name.lower() == 'q':
            break
        if name in contacts:
            print(f"Name : {name}")
            print(f"Phone: {contacts[name]['phone']}")
            print(f"Email: {contacts[name]['email']}\n")
        else:
            print(f"Error: Contact '{name}' not found.\n")

def view_contacts():
    if not contacts:
        print("No contacts available.\n")
        return
    print("All Contacts:")
    print("-" * 40)
    for name, info in contacts.items():
        print(f"Name : {name}")
        print(f"Phone: {info['phone']}")
        print(f"Email: {info['email']}")
        print("-" * 40)
    print()

def update_contact():
    name = input("Enter the contact name to update: ").strip()
    if name not in contacts:
        print(f"Error: Contact '{name}' not found.\n")
        return
    
    new_name = input("Enter new name (press space to keep unchanged): ").strip()
    new_phone = input("Enter new phone (press space to keep unchanged): ").strip()
    new_email = input("Enter new email (press space to keep unchanged): ").strip()
    
    # Update only if input is not empty or only space
    if new_name and new_name != " ":
        contacts[new_name] = contacts.pop(name)
        name = new_name  # update the current reference
    if new_phone and new_phone != " ":
        contacts[name]['phone'] = new_phone
    if new_email and new_email != " ":
        contacts[name]['email'] = new_email
    
    print(f"Contact '{name}' updated successfully.\n")

def main():
    while True:
        print("Contact Management System")
        print("1. Add Contact")
        print("2. Remove Contact")
        print("3. Search Contact")
        print("4. View All Contacts")
        print("5. Update Contact")
        print("6. Exit")
        
        choice = input("Enter your choice: ").strip()
        print()
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            remove_contact()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            view_contacts()
        elif choice == '5':
            update_contact()
        elif choice == '6':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Run the program
if __name__ == "__main__":
    main()
