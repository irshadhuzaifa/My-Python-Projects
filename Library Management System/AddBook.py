from PySimpleGUI import *

def add_book():
    add_layout = [
        [Text("Enter book Title here:", pad=((50, 50), (30, 0)))],
        [Input(size=50, key='-Add 1-', pad=((50, 50), (0, 20)), do_not_clear=False)],
        [Text("Enter book ISBN here:", pad=((50, 50), (20, 0)))],
        [Input(size=50, key='-Add 2-', pad=((50, 50), (0, 20)), do_not_clear=False)],
        [Text("Enter book Author here:", pad=((50, 50), (20, 0)))],
        [Input(size=50, key='-Add 3-', pad=((50, 50), (0, 20)), do_not_clear=False)],
        [Button('Add Book', size=(8, 2), pad=((50, 50), (20, 20)), border_width=4, button_color="Black", expand_x=True)]
        ]

    add_book_window = Window(title="Adding a Book", layout=add_layout)

    return add_book_window()
