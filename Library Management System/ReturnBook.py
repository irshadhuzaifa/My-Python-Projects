from PySimpleGUI import *

def return_book():

    return_layout = [
                [Text("Enter book Title here:", pad=((50, 50), (30, 0)))],
                [Input(size=50, key='-Return-', pad=((50, 50), (0, 20)), do_not_clear=False)],
                [Button('Return Book', size=(8, 2), pad=((50, 50), (20, 20)), border_width=4, button_color="Black", expand_x=True)]
            ]

    return_book_window = Window(title="Return a Book", layout=return_layout)

    return return_book_window()