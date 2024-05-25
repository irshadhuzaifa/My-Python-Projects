from PySimpleGUI import *

def delete_book():

    delete_layout = [
            [Text("Enter book Title here:", pad=((50, 50), (30, 0)))],
            [Input(size=50, key='-Del 1-', pad=((50, 50), (0, 20)), do_not_clear=False)],
            [Text("Enter book ISBN here:", pad=((50, 50), (20, 0)))],
            [Input(size=50, key='-Del 2-', pad=((50, 50), (0, 20)), do_not_clear=False)],
            [Button('Delete Book', size=(8, 2), pad=((50, 50), (20, 20)), border_width=4, button_color="Black", expand_x=True)]
            ]

    delete_book_window = Window(title="Deleting a Book", layout=delete_layout)

    return delete_book_window()
