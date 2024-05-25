from PySimpleGUI import *

def issue_book():

    issue_layout = [
                [Text("Enter book Title here:", pad=((50, 50), (30, 0)))],
                [Input(size=50, key='-Issue-', pad=((50, 50), (0, 20)), do_not_clear=False)],
                [Button('Issue Book', size=(8, 2), pad=((50, 50), (20, 20)), border_width=4, button_color="Black", expand_x=True)]
            ]

    issue_book_window = Window(title="Issue a Book", layout=issue_layout)

    return issue_book_window()
