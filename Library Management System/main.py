
from PySimpleGUI import *
import AddBook
import ViewBooks
import DeleteBook
import IssueBook
import ReturnBook


layout = [
    [Text("Select an Option", expand_x=True, pad=20, border_width=10, text_color="Blue", font="Calibri", justification="center")],
    [Button("Add", size=(6,2), pad=20, border_width=4), Button("View", size=(6,2), pad=20, border_width=4),
     Button("Issue", size=(6,2), pad=20, border_width=4), Button("Return", size=(6,2), pad=20, border_width=4),
     Button("Delete", size=(6,2), pad=20, border_width=4)]
]

window = Window(title="Books Library", layout=layout, button_color="Black", background_color="Light Blue", size=(535,190))

while True:

    event, values = window.read()  # Creates the main window containing buttons of Add, View, Issue, Return and Delete

    if event == WIN_CLOSED:        # If window is closed, the condition breaks the loop and ends the program.
        break

    if event == "Add":
        add_event, add_values = AddBook.add_book()    # Creates the adding book window when Add Book button is clicked.
        book_title = add_values['-Add 1-']
        book_ISBN = add_values['-Add 2-']               # The inputs with the corresponding Keys are stored in the variables.
        book_author = add_values['-Add 3-']

        # Error handling if inputs are left empty, or contains only spaces or the ISBN doesn't contain digits only.
        if (not book_author or book_author.isspace() or not book_title or book_title.isspace()
                or not book_ISBN or book_ISBN.isspace() or not book_ISBN.isdigit()):
            popup('Please enter valid book information.')
        else:
            ViewBooks.books.append([book_title, book_ISBN, book_author, 1])    # Updates the books list in the ViewBooks file.
            popup('Book added successfully!')
        break



    if event == "View":
        ViewBooks.view_books()           # Creates the books list window when the View Books button is clicked.

    if event == "Delete":
        del_event, del_values = DeleteBook.delete_book()            # Creates the delete book window when Delete Book button is clicked.
        del_title = del_values['-Del 1-']
        del_ISBN = del_values['-Del 2-']

        if not del_title or del_title.isspace() :
            popup("The book title field is empty")                     # Gives popup if input fields are emplty or contain only spaces.
            break

        elif not del_ISBN or del_ISBN.isspace():
            popup("The book ISBN field is empty.")
            break

        elif not del_ISBN.isdigit():
            popup("Enter valid ISBN number.")
            break

        deleted = False

        for index_num, (name, isbn, author, number) in enumerate(ViewBooks.books):
            if name == del_title and isbn == del_ISBN:
                ViewBooks.books.pop(index_num)
                popup('Book deleted successfully!')
                deleted = True

        if deleted == False:
            popup("There is no book in our record that matches the information you entered.")

        break


    if event == "Issue":
        issue_event, issue_values = IssueBook.issue_book()
        issued_book = issue_values['-Issue-']

        issued = False

        for item in ViewBooks.books:
            if issued_book == item[0]:
                if item[-1] > 0:
                    item[-1] -= 1                      # If book exists and its quantity is greater tha zero, than book is issued and quantity is decreased by 1.
                    popup('Book issued successfully!')
                    issued = True
                else:
                    popup(f"All {issued_book} books have been issued. Select another book.")    # Gives popup if selected book quantity is zero.
                    issued = True

        if issued == False:           # Error handling if the input value doesn't match any of the book titles in ViewBooks list.
            popup("Book not found")
        break

    if event == "Return":
        return_event, return_values = ReturnBook.return_book()
        returned_book = return_values['-Return-']

        if not returned_book or returned_book.isspace():      # Gives popup if the input field is empty or only contains spaces.
            popup("You didn't enter anything.")
            break

        returned = False

        for index_num, (name, isbn, author, number) in enumerate(ViewBooks.books):
            if returned_book == name:
                ViewBooks.books[index_num][-1] += 1
                popup('Book returned successfully!')
                returned = True

        if returned == False:                   # Gives popup if the entered title is not the ViewBooks list.
            popup("The book title you entered doesn't match any book in our record.")
        break

for book in ViewBooks.books:
    print(book)

