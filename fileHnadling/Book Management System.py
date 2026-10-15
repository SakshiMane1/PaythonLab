def load_books():
    books = []

    try:
        with open("books.txt", "r") as file:
            for line in file:
                book_id, title, author, status = line.strip().split(",")

                books.append({
                    "id": book_id,
                    "title": title,
                    "author": author,
                    "status": status
                })

    except FileNotFoundError:
        pass

    return books


def save_books(books):
    with open("books.txt", "w") as file:
        for book in books:
            file.write(
                book["id"] + "," +
                book["title"] + "," +
                book["author"] + "," +
                book["status"] + "\n"
            )


def add_book():
    books = load_books()

    book_id = input("Enter book ID: ")
    title = input("Enter title: ")
    author = input("Enter author: ")

    books.append({
        "id": book_id,
        "title": title,
        "author": author,
        "status": "Available"
    })

    save_books(books)

    print("Book added successfully.")


def search_book():
    books = load_books()

    book_id = input("Enter book ID: ")

    for book in books:
        if book["id"] == book_id:
            print(book)
            return

    print("Book not found.")


def issue_book():
    books = load_books()

    book_id = input("Enter book ID: ")

    for book in books:
        if book["id"] == book_id:

            if book["status"] == "Available":
                book["status"] = "Issued"
                save_books(books)
                print("Book issued successfully.")
            else:
                print("Book is already issued.")

            return

    print("Book not found.")


def return_book():
    books = load_books()

    book_id = input("Enter book ID: ")

    for book in books:
        if book["id"] == book_id:
            book["status"] = "Available"
            save_books(books)
            print("Book returned successfully.")
            return

    print("Book not found.")


def display_available_books():
    books = load_books()

    print("\nAvailable Books:")

    for book in books:
        if book["status"] == "Available":
            print(book)


while True:

    print("\n--- Library Menu ---")
    print("1. Add Book")
    print("2. Search Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display Available Books")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        search_book()

    elif choice == "3":
        issue_book()

    elif choice == "4":
        return_book()

    elif choice == "5":
        display_available_books()

    elif choice == "6":
        print("Program ended.")
        break

    else:
        print("Invalid choice.")