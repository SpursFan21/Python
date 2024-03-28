from array import array

def add_book(books, book):
    books.append(book.encode('utf-8'))  # Encode the book title to bytes
    print(f"'{book}' has been added to your favorite books.")

def remove_book(books, book):
    try:
        books.remove(book)
        print(f"'{book}' has been removed from your favorite books.")
    except ValueError:
        print(f"'{book}' is not in your favorite books list.")

def view_books(books):
    if books:
        print("Your favorite books:")
        for book in books:
            print("-", book.decode('utf-8'))  # Decode the book title from bytes to Unicode
    else:
        print("Your favorite books list is empty.")

def main():
    favorite_books = array('b', [])  # Creating an array of bytes

    while True:
        print("\n1. Add a book to favorites")
        print("2. Remove a book from favorites")
        print("3. View favorite books")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            book = input("Enter the name of the book you want to add: ")
            add_book(favorite_books, book)
        elif choice == '2':
            book = input("Enter the name of the book you want to remove: ")
            remove_book(favorite_books, book.encode('utf-8'))  # Encode book title before removing
        elif choice == '3':
            view_books(favorite_books)
        elif choice == '4':
            print("Thank you for using the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
