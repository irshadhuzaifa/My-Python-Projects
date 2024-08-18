from turtle import *
from positional_linked_list import PositionalList

FONT = ("Times New Roman", 12, "normal")
SPACING = 10


class Letters():

    class Pointer():

        def __init__(self):
            self.cursor = Turtle()
            self.cursor.hideturtle()
            self.cursor.shape("square")
            self.cursor.penup()
            self.cursor.speed(0)
            self.cursor.shapesize(stretch_wid=1, stretch_len=0.01)
            self.cursor.goto(-300, 210)
            self._x = -300
            self._y = 210

        def unhide_turtle(self):
            self.cursor.showturtle()

        def update_position(self):
            self.cursor.goto(self._x, self._y)  # Update cursor position


    def __init__(self):
        self.screen = Screen()
        self.screen.bgcolor("white")
        self.screen.setup(height=600, width=800)
        self.screen.title("Text Editor")
        self.screen.tracer(0)  # Disable automatic updates

        self.writer = Turtle()
        self.writer.hideturtle()
        self.writer.penup()
        self.writer_x = -300
        self.writer_y = 200
        self.writer.goto(self.writer_x, self.writer_y)
        self.writer.pendown()
        self.writer.speed(0)         # Set the turtle speed to maximum (0 is the fastest)

        self.pointer = self.Pointer()
        self.pointer.unhide_turtle()
        self.positions = PositionalList()
        self.current_pos = None

        self.screen.update()

        self.header_pos = self.positions.header_position()
        self.trailer_pos = self.positions.trailer_position()

    # Function to move the cursor to the right and to change the current_pos to the right in
    # the positional list.
    def move_right(self):

        if self.pointer._x  >= 260 and self.pointer._y >= -190:
            self.pointer._x = -300
            self.pointer._y -= 20
            self.pointer.update_position()
            self.screen.update()

        elif self.current_pos != self.positions.last():
            if self.current_pos == self.header_pos:
                self.current_pos = self.positions.first()
                self.pointer._x += 10
                self.pointer.update_position()
                self.screen.update()
            else:
                self.current_pos = self.positions.after(self.current_pos)
                self.pointer._x += 10
                self.pointer.update_position()
                self.screen.update()

    # Function to move the cursor to the left and to change the current_pos to the left in
    # the positional list.
    def move_left(self):

        if self.pointer._x < -290 and self.pointer._y < 210:
            self.pointer._x = 260
            self.pointer._y += 20
            self.pointer.update_position()
            self.screen.update()

        else:

            if self.current_pos == None:
                self.current_pos = self.header_pos

            elif self.current_pos.element() != None:
                self.current_pos = self.positions.before(self.current_pos)
                self.pointer._x -= 10
                self.pointer.update_position()
                self.screen.update()

    # Function to move the cursor upward by one line and to change the current_pos to the upward line in
    # the positional list.
    def move_up(self):
        if self.pointer._y < 210:
            for _ in range(56):
                self.current_pos = self.positions.before(self.current_pos)
            self.pointer._y += 20
            self.pointer.update_position()
            self.screen.update()

    # Function to move the cursor downward by one line and to change the current_pos to the downward line in
    # the positional list. If lines are incomplete, the function fills the remaining positions in the positional list
    # and the screen with sapces.
    def move_down(self):


        if self.current_pos == self.header_pos:

            if self.positions.__len__() == 0:
                self.enter()

            elif self.positions.__len__() < 56:

                while self.positions.__len__() != 56:
                    self.positions.add_last(" ")
                self.current_pos = self.positions.last()
                self.rewrite_list()
                self.pointer._x = -300
                self.pointer._y -= 20
                self.pointer.update_position()

                self.writer.penup()
                self.writer_y -= 20
                self.writer.goto(self.writer_x, self.writer_y)
                self.writer.pendown()
                self.screen.update()

            else:
                self.current_pos = self.positions.first()
                for _ in range(55):
                    self.current_pos = self.positions.after(self.current_pos)

                self.pointer._x = -300
                self.pointer._y -= 20
                self.pointer.update_position()
                self.screen.update()

        elif self.current_pos == self.positions.last():
            self.enter()

        else:
            count_nex = self.positions.__len__() % 56
            temp_pos = self.current_pos
            while temp_pos != self.positions.last():
                temp_pos = self.positions.after(temp_pos)
                count_nex += 1

            if count_nex < 56:
                    while self.positions.__len__() % 56 != 0:
                        self.positions.add_last(" ")
                    while self.current_pos != self.positions.last():
                        self.current_pos = self.positions.after(self.current_pos)
                    self.rewrite_list()
                    self.pointer._x = -300
                    self.pointer.update_position()

                    self.writer.penup()
                    self.writer_y -= 20
                    self.writer.goto(self.writer_x, self.writer_y)
                    self.writer.pendown()

            else:

                try:
                    for _ in range(56):
                        self.current_pos = self.positions.after(self.current_pos)

                except:
                    self.current_pos = self.positions.last()
                    self.rewrite_list()
                    self.pointer._x = self.writer.xcor()

            if self.pointer._y > -190:
                self.pointer._y -= 20
                self.pointer.update_position()

            self.screen.update()

    # Function to insert text on the screen and move the turtle 'writer' forward.
    def insert_text(self, char):
        self.writer.penup()
        self.writer.forward(SPACING)
        self.writer.goto(self.pointer._x, self.writer_y)
        self.writer.pendown()
        self.writer.write(char, font=FONT)
        self.screen.update()

    # Function to write the last positional list element on the screen and move the turtle 'writer' forward while doing so.
    def render_text(self):
        pos = self.positions.last()
        self.writer.write(pos.element(), font=FONT)
        self.writer.penup()
        self.writer.forward(SPACING)
        self.writer.pendown()
        self.screen.update()


    # Function to write any letter pressed on the keyboard on the screen. Basically the function takes the letter parameter,
    # add it the positional list at wherever the cursor is using the current_pos variable and updates the positional list,
    # finally the the function rewrites the whole positional list and updates the screen.
    def write_letter(self, letter):

        if self.positions.__len__() < 1120:

            if -300 <= self.pointer._x <= 260 and -190 <= self.pointer._y <= 210:

                self.pointer.cursor.hideturtle()
                self.pointer._x += 10


                if self.pointer._x > 260:
                    self.pointer._x = -290
                    self.pointer._y -= 20
                    self.writer_y -= 20
                    self.writer.penup()
                    self.writer.goto(self.writer_x, self.writer_y)
                    self.writer.pendown()

                self.pointer.update_position()
                self.pointer.unhide_turtle()

                if self.positions.__len__() <= 2:

                    # Store letter in the positional list and store the letter's position in variable
                    new_pos = self.positions.add_last(letter)
                    # Update current position
                    self.current_pos = new_pos
                    self.render_text()

                elif self.current_pos == self.header_pos or self.positions.after(self.current_pos) != None:


                    if self.current_pos == self.header_pos:
                        self.current_pos = self.positions.add_first(letter)
                        self.rewrite_list()

                    else:
                        curr_node = self.positions.validate(self.current_pos)

                        new_node = self.positions.insert_between(letter, curr_node, curr_node.next)

                        self.rewrite_list()
                        self.current_pos = self.positions.after(self.current_pos)

                else:
                    # Store letter in the positional list and store the letter's position in variable
                    new_pos = self.positions.add_last(letter)
                    # Update current position
                    self.current_pos = new_pos
                    self.render_text()

    # Writes space
    def write_space(self):
        self.write_letter(" ")

    # Move the cursor to the next line start.
    def next_line(self):
        self.pointer._y -= 20
        self.pointer._x = -300
        self.pointer.update_position()

    # Writes spaces at the end of the line if there are empty positions.
    def write_blank_last(self, num_blank):
        for _ in range(num_blank):
            new_pos = self.positions.add_last(" ")
            self.current_pos = new_pos
        self.rewrite_list()
        self.writer.penup()
        self.writer.goto(self.pointer._x, self.pointer._y - 10)
        self.writer.pendown()
        self.screen.update()


    # Writes spaces at the beginning line when the user wishes to move the cursor without writing anything.
    def write_blank_first(self, num_blank):
        for _ in range(num_blank):
            new_pos = self.positions.add_first(" ")
            self.current_pos = new_pos
        self.rewrite_list()
        self.writer.penup()
        self.writer.goto(self.pointer._x, self.pointer._y - 10)
        self.writer.pendown()
        self.screen.update()


    # Writes spaces in between letters when the user wishes to move a part of text downward by pressing enter.
    def write_blank_between(self, num_blank):

        for _ in range(num_blank):
            current_node = self.positions.validate(self.current_pos)
            next_pos = self.positions.insert_between(" ", current_node, current_node.next)
            self.current_pos = next_pos

        self.rewrite_list()

    # Uses the write_blank_last , write_blank_first and write_blank_between functions to move the cursor and elements
    # in the positional list like pressing enter on any other text editor.
    def enter(self):
        if self.positions.__len__() < 1120:
            if self.pointer._y > -190:
                self.next_line()
                self.writer.penup()
                self.writer_y -= 20
                self.writer.goto(self.writer_x, self.writer_y)
                self.writer.pendown()
                self.screen.update()


            if self.current_pos == self.header_pos:

                if self.positions.__len__()==0:
                    num_spaces = 56
                    self.write_blank_last(num_spaces)
                    self.screen.update()

                else:
                    self.write_blank_first(56)

            elif self.current_pos == self.positions.last():
                prev_pos = self.positions.before(self.current_pos)
                if prev_pos.element() == " ":
                    self.write_blank_last(56)
                else:
                    count_prev = self.positions.__len__() % 56
                    spaces_num = 56 - count_prev
                    self.write_blank_last(spaces_num)

            else:
                curr_pos = self.current_pos
                count_prev = 0

                if self.pointer._y == 190:
                    count_prev = 1
                    while curr_pos != self.positions.first():
                        curr_pos = self.positions.before(curr_pos)
                        count_prev += 1
                    num_of_spaces = 56 - count_prev
                    self.write_blank_between(num_of_spaces)

                else:
                    count_prev = 0
                    while curr_pos.element() != " ":
                        curr_pos = self.positions.before(curr_pos)
                        count_prev += 1
                    num_of_spaces = 56 - count_prev
                    self.write_blank_between(num_of_spaces)

    # Moves the cursor backward, removes the letter just before the current_pos from the positional list and
    # rewrites the whole list.
    def backspace(self):

        if self.pointer._y < 210 and self.pointer._x <= -300:
            self.pointer._y += 20
            self.pointer._x = 260
            self.pointer.update_position()
            self.screen.update()

        if self.current_pos == self.header_pos:
            return

        if self.current_pos == self.positions.first():
            self.positions.delete(self.current_pos)
            self.pointer._x -= 10
            self.pointer.update_position()
            self.rewrite_list()
            self.screen.update()
            self.current_pos = self.header_pos

        else:

            self.pointer._x -= 10
            self.pointer.update_position()

            self.current_pos = self.positions.before(self.current_pos)
            self.positions.delete(self.positions.after(self.current_pos))
            self.rewrite_list()


# Functions for each letter of the keyboard which pass the corresponding letter to the write_letter function.
    def write_a(self):
        self.write_letter("a")

    def write_b(self):
        self.write_letter("b")

    def write_c(self):
        self.write_letter("c")

    def write_d(self):
        self.write_letter("d")

    def write_e(self):
        self.write_letter("e")

    def write_f(self):
        self.write_letter("f")

    def write_g(self):
        self.write_letter("g")

    def write_h(self):
        self.write_letter("h")

    def write_i(self):
        self.write_letter("i")

    def write_j(self):
        self.write_letter("j")

    def write_k(self):
        self.write_letter("k")

    def write_l(self):
        self.write_letter("l")

    def write_m(self):
        self.write_letter("m")

    def write_n(self):
        self.write_letter("n")

    def write_o(self):
        self.write_letter("o")

    def write_p(self):
        self.write_letter("p")

    def write_q(self):
        self.write_letter("q")

    def write_r(self):
        self.write_letter("r")

    def write_s(self):
        self.write_letter("s")

    def write_t(self):
        self.write_letter("t")

    def write_u(self):
        self.write_letter("u")

    def write_v(self):
        self.write_letter("v")

    def write_w(self):
        self.write_letter("w")

    def write_x(self):
        self.write_letter("x")

    def write_y(self):
        self.write_letter("y")

    def write_z(self):
        self.write_letter("z")


    # Function to clear screen and write all the letter in the positional list all over again on the screen.
    def rewrite_list(self):

        self.writer.clear()
        self.writer.penup()
        self.writer_x = -300
        self.writer_y = 200
        self.writer.goto(self.writer_x, self.writer_y)
        self.writer.pendown()

        for element in self.positions:

            if self.writer.xcor() > 250:

                self.writer.penup()
                self.writer_y -= 20
                self.writer.goto(self.writer_x, self.writer_y)
                self.writer.pendown()
                self.writer.write(element, font=FONT)
                self.writer.penup()
                self.writer.forward(SPACING)
                self.writer.pendown()

            else:
                self.writer.write(element, font=FONT)
                self.writer.penup()
                self.writer.forward(SPACING)
                self.writer.pendown()

        self.screen.update()

# Create an instance of the Letters class
letter = Letters()

letter.screen.listen()

# Bind each alphabet key to its corresponding function
letter.screen.onkeypress(letter.write_a, "a")
letter.screen.onkeypress(letter.write_b, "b")
letter.screen.onkeypress(letter.write_c, "c")
letter.screen.onkeypress(letter.write_d, "d")
letter.screen.onkeypress(letter.write_e, "e")
letter.screen.onkeypress(letter.write_f, "f")
letter.screen.onkeypress(letter.write_g, "g")
letter.screen.onkeypress(letter.write_h, "h")
letter.screen.onkeypress(letter.write_i, "i")
letter.screen.onkeypress(letter.write_j, "j")
letter.screen.onkeypress(letter.write_k, "k")
letter.screen.onkeypress(letter.write_l, "l")
letter.screen.onkeypress(letter.write_m, "m")
letter.screen.onkeypress(letter.write_n, "n")
letter.screen.onkeypress(letter.write_o, "o")
letter.screen.onkeypress(letter.write_p, "p")
letter.screen.onkeypress(letter.write_q, "q")
letter.screen.onkeypress(letter.write_r, "r")
letter.screen.onkeypress(letter.write_s, "s")
letter.screen.onkeypress(letter.write_t, "t")
letter.screen.onkeypress(letter.write_u, "u")
letter.screen.onkeypress(letter.write_v, "v")
letter.screen.onkeypress(letter.write_w, "w")
letter.screen.onkeypress(letter.write_x, "x")
letter.screen.onkeypress(letter.write_y, "y")
letter.screen.onkeypress(letter.write_z, "z")
letter.screen.onkeypress(letter.write_space, "space")
letter.screen.onkeypress(letter.backspace, "BackSpace")
letter.screen.onkeypress(letter.enter, "Return")



letter.screen.onkeypress(letter.move_right, "Right")
letter.screen.onkeypress(letter.move_left, "Left")
letter.screen.onkeypress(letter.move_up, "Up")
letter.screen.onkeypress(letter.move_down, "Down")



letter.screen.exitonclick()