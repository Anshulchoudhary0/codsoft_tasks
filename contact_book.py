class ContactBook:

    def __init__(self):
        self.contacts = []

    def add_contact(self):
        print("\n--- Add New Contact ---")
        name = input("Enter Name: ").strip()
        phone = input("Enter Phone Number: ").strip()
        email = input("Enter Email: ").strip()
        address = input("Enter Address: ").strip()

        if not name or not phone:
            print("Name and Phone Number are required.")
            return

        self.contacts.append(
            {"name": name, "phone": phone, "email": email, "address": address}
        )
        print(f"Contact '{name}' added successfully!")

    def view_contacts(self):
        print("\n--- Contact List ---")
        if not self.contacts:
            print("No contacts saved yet.")
            return

        for idx, contact in enumerate(self.contacts, 1):
            print(
                f"{idx}. Name: {contact['name']} | Phone: {contact['phone']}"
            )

    def search_contact(self):
        print("\n--- Search Contact ---")
        query = (
            input("Enter name or phone number to search: ").strip().lower()
        )
        results = [
            c
            for c in self.contacts
            if query in c["name"].lower() or query in c["phone"]
        ]

        if not results:
            print("No matching contacts found.")
            return

        print(f"\nFound {len(results)} matching contact(s):")
        for contact in results:
            self._display_full_contact(contact)

    def update_contact(self):
        print("\n--- Update Contact ---")
        name = input("Enter the name of the contact to update: ").strip().lower()
        for contact in self.contacts:
            if contact["name"].lower() == name:
                print("Leave field blank to keep current value.")
                new_phone = input(f"New Phone [{contact['phone']}]: ").strip()
                new_email = input(f"New Email [{contact['email']}]: ").strip()
                new_address = input(
                    f"New Address [{contact['address']}]: "
                ).strip()

                if new_phone:
                    contact["phone"] = new_phone
                if new_email:
                    contact["email"] = new_email
                if new_address:
                    contact["address"] = new_address

                print("Contact updated successfully!")
                return
        print("Contact not found.")

    def delete_contact(self):
        print("\n--- Delete Contact ---")
        name = input("Enter the name of the contact to delete: ").strip().lower()
        for idx, contact in enumerate(self.contacts):
            if contact["name"].lower() == name:
                confirm = (
                    input(
                        f"Are you sure you want to delete {contact['name']}? (y/n): "
                    )
                    .strip()
                    .lower()
                )
                if confirm == "y":
                    deleted = self.contacts.pop(idx)
                    print(f"Contact '{deleted['name']}' deleted successfully.")
                return
        print("Contact not found.")

    def _display_full_contact(self, contact):
        print("-" * 30)
        print(f"Name:    {contact['name']}")
        print(f"Phone:   {contact['phone']}")
        print(f"Email:   {contact['email']}")
        print(f"Address: {contact['address']}")
        print("-" * 30)


def main():
    book = ContactBook()
    while True:
        print("\n==============================")
        print("         CONTACT BOOK         ")
        print("==============================")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            book.add_contact()
        elif choice == "2":
            book.view_contacts()
        elif choice == "3":
            book.search_contact()
        elif choice == "4":
            book.update_contact()
        elif choice == "5":
            book.delete_contact()
        elif choice == "6":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid number between 1 and 6.")


if __name__ == "__main__":
    main()
