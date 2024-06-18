
contact_book = []

def create_contact():
    while True:
        name = input("Name: ")
        email = input("Email: ")
        number = input("Number: ")

        contact = {
            "name" : name,
            "email" : email,
            "number" : number
    }

        contact_book.append(contact)
        print("Contact successfully added")
        add_contact = input("Too add another contact press y, to continue press enter: ").lower()
        if add_contact == "y":
            continue
        elif add_contact == "":
            break
        else:
            print("Invalid input")
    return(contact_book)

def find_contact():
    if not contact_book:
        print("No contacts, please add contacts")
    else:
        person = input("Who do you want to find?: ")
        for contact in contact_book:
            if contact["name"] == person:
                print(f"Name: {contact['name']}")
                print(f"Email: {contact['email']}")
                print(f"Number: {contact['number']}")
            else:
                print("Contact does not exist")

def update_contact():
    if not contact_book:
        print("No contacts, please add contacts")
    else:
        person = input("What contact do you want to update?: ")
        for contact in contact_book:
            if contact["name"] == person:
                new_name = (input('New name: '))
                new_email = (input('New email: '))
                new_number =(input('New number: '))

                if new_name:
                    contact["name"] = new_name
                if new_email:
                    contact["email"] = new_email
                if new_number:
                    contact["number"] = new_number

                print("Contact updated successfully")
                return
        print("Contact not found")

def delete_contact():
    if not contact_book:
        print("No contacts, please add contacts")
    else:
        person = input("Who do you want to delete?: ")
        for i, contact in enumerate(contact_book):
            if contact["name"] == person:
                del contact_book[i]
                print("Contact successfully removed")
                return
            else:
                print("Contact not found")


def main():
    while True:
        action = input("To create a contact press [1], to find a contact press [2], to view contacts press [3], to update a contact press [4], to delete contact press [5] to exit press [6]: ")
        if action == "1":
            create_contact()
        elif action == "2":
            find_contact()
        elif action == "3":
            if not contact_book:
                print("No contacts exist, please add contacts")
            for contact in contact_book:
                print(f"Name: {contact['name']}")
                print(f"Email: {contact['email']}")
                print(f"Number: {contact['number']}")
                print()
        elif action == "4":
            update_contact()
        elif action == "5":
            delete_contact()
        elif action == "6":
            break
        else:
            print("Invalid number")

if __name__ == "__main__":
    main()

