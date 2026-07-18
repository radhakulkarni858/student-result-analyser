# Function to add a book to the catalog
def add_book(catalog, book_id, title, author, year):
    catalog[book_id] = (title, author, year)


# Function to borrow a book
def borrow_book(catalog, borrowed_books, book_id):
    if book_id in catalog:
        if book_id not in borrowed_books:
            borrowed_books.append(book_id)
            print(f"Book {book_id} borrowed successfully.")
        else:
            print(f"Book {book_id} is already borrowed.")
    else:
        print(f"Book {book_id} does not exist.")


# Function to return a book
def return_book(borrowed_books, book_id):
    if book_id in borrowed_books:
        borrowed_books.remove(book_id)
        print(f"Book {book_id} returned successfully.")
    else:
        print(f"Book {book_id} was not borrowed.")


# Function to register a member
def register_member(members, member_id):
    members.add(member_id)   # Set automatically ignores duplicates


# Function to display available books
def show_available(catalog, borrowed_books):
    print("\nAvailable Books:")
    found = False

    for book_id, details in catalog.items():
        if book_id not in borrowed_books:
            title, author, year = details
            print(f"Book ID: {book_id}")
            print(f"Title   : {title}")
            print(f"Author  : {author}")
            print(f"Year    : {year}")
            print("-" * 30)
            found = True

    if not found:
        print("No books available.")


# Main function
def main():
    # Required data structures
    catalog = {}            # Dictionary
    borrowed_books = []     # List
    members = set()         # Set

    # Add 4 books
    add_book(catalog, 101, "Python Basics", "John Smith", 2020)
    add_book(catalog, 102, "Data Structures", "Alice Brown", 2021)
    add_book(catalog, 103, "Machine Learning", "Andrew Ng", 2022)
    add_book(catalog, 104, "Artificial Intelligence", "Stuart Russell", 2019)

    # Register 3 members
    register_member(members, 1001)
    register_member(members, 1002)
    register_member(members, 1003)

    # Try adding the same member again (ignored)
    register_member(members, 1002)

    # Borrow 2 books
    borrow_book(catalog, borrowed_books, 101)
    borrow_book(catalog, borrowed_books, 103)

    # Return 1 book
    return_book(borrowed_books, 101)

    # Display available books
    show_available(catalog, borrowed_books)

    # Display members and borrowed books
    print("Registered Members:", members)
    print("Borrowed Books:", borrowed_books)


# Run the program
if __name__ == "__main__":
    main()
