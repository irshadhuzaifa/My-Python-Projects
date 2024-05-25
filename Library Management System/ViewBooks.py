from PySimpleGUI import *

books = [
    ["The Great Gatsby", "9780743273565", "F. Scott Fitzgerald", 5],
    ["1984", "9780451524935", "George Orwell", 3],
    ["To Kill a Mockingbird", "9780061120084", "Harper Lee", 4],
    ["Pride and Prejudice", "9780141040349", "Jane Austen", 2],
    ["The Catcher in the Rye", "9780316769488", "J.D. Salinger", 6],
    ["The Hobbit", "9780547928227", "J.R.R. Tolkien", 5],
    ["Moby Dick", "9781503280786", "Herman Melville", 0],
    ["War and Peace", "9780199232765", "Leo Tolstoy", 3],
    ["Ulysses", "9780199535675", "James Joyce", 2],
    ["The Odyssey", "9780140268867", "Homer", 4],
    ["The Brothers Karamazov", "9780374528379", "Fyodor Dostoevsky", 2],
    ["Crime and Punishment", "9780143058144", "Fyodor Dostoevsky", 3],
    ["Brave New World", "9780060850524", "Aldous Huxley", 4],
    ["The Divine Comedy", "9780140448955", "Dante Alighieri", 2],
    ["Anna Karenina", "9780143035008", "Leo Tolstoy", 3]
]

def view_books():

    view_layout = [
        [Text("Title", size=(20, 1), justification="centre"),
         Text("ISBN", size=(20, 1), justification="centre"),
         Text("Author", size=(20, 1), justification="centre"),
         Text("Availability", size=(20, 1), justification="centre")],
        [HorizontalSeparator()]
    ]

    for book in books:
        view_layout.append(
            [Text(book[0], size=(20, 1), justification="centre"),
             Text(book[1], size=(20, 1), justification="centre"),
             Text(book[2], size=(20, 1), justification="centre"),
             Text(book[3], size=(20, 1), justification="centre")])

    view_book_window = Window(title="Viewing available Books", layout=view_layout, auto_size_text=True)

    return view_book_window()