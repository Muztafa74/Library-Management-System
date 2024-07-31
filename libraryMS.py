books = []
members = []
borrowed_books = {}


def add_book(book_name):
    if book_name in books:
        print("Book already exists")
    else:
        books.append(book_name)
        print(f'Book "{book_name}" added to the library.')


def register_member(member_name):
    if member_name in members:
        print("Member already registered")
    else:
        members.append(member_name)
        borrowed_books[member_name] = []
        print(f'Member "{member_name}" registered.')


def borrow_book(member_name, book_name):
    if member_name not in members:
        print("Member not registered")
        return
    if book_name not in books:
        print("Book not available in the library")
        return
    if book_name in borrowed_books[member_name]:
        print(f'Member {member_name} has already borrowed {book_name}')
        return
    
    borrowed_books[member_name].append(book_name)
    books.remove(book_name)
    print(f'Book {book_name} borrowed by member {member_name}.')


def return_book(member_name, book_name):
    if member_name not in members:
        print("Member not registered")
        return
    if book_name not in borrowed_books[member_name]:
        print(f'Member {member_name} did not borrow {book_name}')
        return

    borrowed_books[member_name].remove(book_name)
    books.append(book_name)
    print(f'Book {book_name} returned by member {member_name}.')


def generate_report():
    print("\nLibrary Report")
    print("--------------")
    print("Available Books:")
    for book in books:
        print(f' - {book}')
    
    print("\nBorrowed Books:")
    for member, borrowed in borrowed_books.items():
        if borrowed:
            print(f'{member} has borrowed:')
            for book in borrowed:
                print(f' - {book}')
        else:
            print(f'{member} has not borrowed any books.')
    
    print("\nRegistered Members:")
    for member in members:
        print(f' - {member}')
    print("--------------\n")


def main():
    while True:
        print("\nLibrary Management System")
        print("1- Add Book")
        print("2- Register Member")
        print("3- Borrow Book")
        print("4- Return Book")
        print("5- Generate Report")
        print("6- Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            book_name = input("Enter Book Name: ")
            add_book(book_name)
        elif choice == "2":
            member_name = input("Enter Member Name: ")
            register_member(member_name)
        elif choice == "3":
            member_name = input("Enter Member Name: ")
            book_name = input("Enter Book Name: ")
            borrow_book(member_name, book_name)
        elif choice == "4":
            member_name = input("Enter Member Name: ")
            book_name = input("Enter Book Name: ")
            return_book(member_name, book_name)
        elif choice == "5":
            generate_report()
        elif choice == "6":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
