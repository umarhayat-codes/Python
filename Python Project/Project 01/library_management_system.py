# books = []

# def add_book(title, author):
#     """Add a book to the library"""
#     books.append({"title": title, "author": author, "borrowed": False})
#     print(f"Book '{title}' by {author} added to the library.")


# def view_books():
#     """View all books in the library"""
#     if not books:
#         print("The library is empty.")
#     else:
#         print("Books in the library:")
#         for book in books:
#             print(f"{book['title']} by {book['author']} [{'Available' if not book['borrowed'] else 'Borrowed'}]")


# def search_by_title(title):
#     """Search for books by title"""
#     found_books = [book for book in books if title.lower() in book['title'].lower()]
#     if found_books:
#         print("Matching books found:")
#         for book in found_books:
#             print(f"{book['title']} by {book['author']} [{'Available' if not book['borrowed'] else 'Borrowed'}]")
#     else:
#         print("No books found with that title.")


# def search_by_author(author):
#     """Search for books by author"""
#     found_books = [book for book in books if author.lower() in book['author'].lower()]
#     if found_books:
#         print("Books by the author found:")
#         for book in found_books:
#             print(f"{book['title']} by {book['author']} [{'Available' if not book['borrowed'] else 'Borrowed'}]")
#     else:
#         print("No books found by that author.")


# def borrow_book(title):
#     """Borrow a book"""
#     for book in books:
#         if book['title'].lower() == title.lower():
#             if not book['borrowed']:
#                 book['borrowed'] = True
#                 print(f"Book '{title}' borrowed successfully.")
#             else:
#                 print(f"Book '{title}' is already borrowed.")
#             return
#     print("Book not found in the library.")



        
# def return_book(title):
#     """Return a borrowed book"""
#     for book in books:
#         if book['title'].lower() == title.lower():
#             if book['borrowed']:
#                 book['borrowed'] = False
#                 print(f"Book '{title}' returned successfully.")
#             else:
#                 print(f"Book '{title}' is already in the library.")
#             return
#     print("Book not found in the library.")


        
# def main():
#     while True:
#         print("\n1. Add Book")
#         print("2. View Books")
#         print("3. Search by Title")
#         print("4. Search by Author")
#         print("5. Borrow Book")
#         print("6. Return Book")
#         print("7. Quit")

#         choice = input("Enter your choice (1-7): ")

#         if choice == '1':
#             title = input("Enter the title of the book: ")
#             author = input("Enter the author of the book: ")
#             add_book(title, author)
#         elif choice == '2':
#             view_books()
#         elif choice == '3':
#             title = input("Enter the title to search for: ")
#             search_by_title(title)
#         elif choice == '4':
#             author = input("Enter the author to search for: ")
#             search_by_author(author)
#         elif choice == '5':
#             title = input("Enter the title of the book to borrow: ")
#             borrow_book(title)
#         elif choice == '6':
#             title = input("Enter the title of the book to return: ")
#             return_book(title)
#         elif choice == '7':
#             print("Exiting program...")
#             break
#         else:
#             print("Invalid choice. Please enter a number between 1 and 7.")

# if __name__ == "__main__":
#     main()



books = []

def addBook(title,author):
    books.append({
        "title" : title,
        "author" : author,
        "borrowed" : False
    })
    print(f"Book '{title}' by '{author}' successfull added: " )


def viewBooks():
    if not books:
        print("Not book found: ")
    else:
        for book in books:
            print(f"Book '{book['title']}' by '{book['author']}' [{'Available' if not book else 'Borrowed'}] ")

def searchByTitle(title):
    foundsBook = [book for book in books if book['title'] in title.lower()]
    if foundsBook:
        print("Matching Search Book: ")
        for book in foundsBook:
            print(f"Book '{book['title']}' by {book['author']} [{'Available' if not book['borrowed'] else 'borrowed'}]")

def borrowedBook(title):
    for book in books:
        if book['title'] == title.lower():
            if not book['borrowed']:
                book['borrowed'] = True
                print(f"Book '{title}' successfuly borrowed")
            else:
                print(f"Book '{title}' already borrowed")
            return
    print("Book not found in the library: ")

    
def returnBook(title):
    for book in books:
        if book['title'] == title.lower():
            if book['borrowed']:
                book['borrowed'] = False
                print(f"Book '{title}' successfully return")
            else: 
                print(f"Book '{title}' already return")
            return
    print(f'Book not bound in the library: ')
    