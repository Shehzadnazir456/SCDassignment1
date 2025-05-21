class Person:
    def __init__(self, name=" ", person_type=" "):
        self.name = name
        self.person_type = person_type

    def introduce(self):
        if self.person_type == "staff":
            print("He is a librarian")
        elif self.person_type == "borrower":
            print("He is a borrower")


class Member(Person):
    def __init__(self, books_borrowed=None, name=" ", person_type="borrower"):
        super().__init__(name, person_type)
        if books_borrowed is None:
            books_borrowed = []
        self.books_borrowed = books_borrowed

    def borrow_book(self, inventory, librarian):
        if len(self.books_borrowed) >= 3:
            print("You have exceeded the limit to borrow books.")
            return
        else:
            book = input("Choose the name of the book you want to borrow: ")
            librarian.issue_book(self, inventory, book)
            

    def return_book(self, inventory):
        while True:
            book = input("Which book do you want to return ? ")
            if book in self.books_borrowed:
                self.books_borrowed.remove(book)
                inventory.append(book)
                print(f"You have returned the book named: {book}")
                break
            else:
                print(f"This book '{book}' is not borrowed by you.")
                continue


class Staff(Person):
    def __init__(self, name=" ", person_type="staff"):
        super().__init__(name, person_type)

    def introduce(self):
        self.person_type = "staff"
        super().introduce()


class Librarian(Staff):
    def __init__(self, name=" ", person_type="Librarian"):
        super().__init__(name, person_type)

    def issue_book(self, member:Member, inventory, book):
        if len(member.books_borrowed) >= 3:
            print("You have exceeded the number of books you can borrow which is three !.")
        elif book in inventory:
            member.books_borrowed.append(book)
            inventory.remove(book)
            print(f"You have borrowed the book named: {book}")
        else:
            print("This book is not present in the inventory.")


class Manager(Staff):
    def __init__(self, name=" ", person_type="Manager", inventory=None):
        super().__init__(name, person_type)
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory

    def manage_inventory(self):
        while True:
            check = input("Do you want to add the inventory : add / remove / exit :").lower().strip()
            if check == "add":
                book = input("Name the book you want to add in inventory :")
                self.inventory.append(book)
                print(f"{book} has been added to inventory")
                
                while True:
                    add = input("Do you want to add the inventory : y/n :").lower().strip()
                    if add == "y":
                        book = input("Name the book you want to add in inventory :")
                        self.inventory.append(book)
                        print(f"{book} has been added to inventory")
                    else:
                        break
                    
            elif check == "remove":
                book = input("Name the book you want to add in inventory :")
                if book in self.inventory:
                    self.inventory.remove(book)
                    print(f"{book} has been remove from inventory")
            elif check == "exit":
                print("Existing the inventory management system")
                break
            else:
                print("You have entered the wrong command . Plz Enter : ADD / REMOVE OR EXIT")  
        


manager = Manager()
manager.manage_inventory()

# Display the current inventory
print("\nCurrent inventory:", manager.inventory)


librarian = Librarian()

# Create a member and allow them to borrow a book from the inventory
member = Member()
member.introduce()
member.borrow_book(manager.inventory, librarian)

# Display the current inventory and borrowed books
print("\nUpdated inventory:", manager.inventory)
print("Borrowed books:", member.books_borrowed)


member.return_book(manager.inventory)

# Display the current inventory and borrowed books after returning
print("\nFinal inventory:", manager.inventory)
print("Borrowed books:", member.books_borrowed)
