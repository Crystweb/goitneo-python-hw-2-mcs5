class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Invalid phone number format")
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        try:
            phone_obj = Phone(phone)
            self.phones.append(phone_obj)
        except ValueError as e:
            print(e)

    def delete_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                return True
        return False

    def edit_phone(self, new_phone):
        self.phones = [Phone(new_phone)]

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(str(p) for p in self.phones)}"

class AddressBook:
    def __init__(self):
        self.data = {}

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, None)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
            return True
        return False

    def edit_phone(self, name, new_phone):
        record = self.find(name)
        if record:
            record.edit_phone(new_phone)
            return True
        return False

def main():
    book = AddressBook()

    while True:
        print("\nAvailable commands:")
        print("1. add - Add a new contact")
        print("2. search - Search for a contact")
        print("3. delete - Delete a contact")
        print("4. edit - Edit a contact's phone number")
        print("5. show - Show all contacts")
        print("6. exit - Exit the program")

        choice = input("Enter your choice: ").strip().lower()

        if choice == "add":
            name = input("Enter contact name: ").strip()
            phone = input("Enter contact phone number: ").strip()
            record = Record(name)
            record.add_phone(phone)
            book.add_record(record)
            print("Contact added.")

        elif choice == "search":
            name = input("Enter contact name to search: ").strip()
            contact = book.find(name)
            if contact:
                print(contact)
            else:
                print("Contact not found.")

        elif choice == "delete":
            name = input("Enter contact name to delete: ").strip()
            if book.delete(name):
                print("Contact deleted.")
            else:
                print("Contact not found.")

        elif choice == "edit":
            name = input("Enter contact name to edit: ").strip()
            new_phone = input("Enter new phone number: ").strip()
            if book.edit_phone(name, new_phone):
                print("Phone number updated.")
            else:
                print("Contact not found.")

        elif choice == "show":
            if not book.data:
                print("Address book is empty.")
            else:
                print("Address book contents:")
                for name, record in book.data.items():
                    print(record)

        elif choice == "exit":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please choose from the available commands.")

if __name__ == "__main__":
    main()
