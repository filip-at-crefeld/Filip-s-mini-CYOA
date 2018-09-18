"""Filip's version of a basic CYOA"""


def print_out_current_page(page_number):
    # TODO: Print to the console the text from that page. Include the choices like 1) xxx 2) xxx.
    if page_number == 0:
        print("yay")
    elif page_number == 1:
        print("nah")


def get_integer_from_player():
    # TODO: Use input function to get a string, make sure it's a number, then return an int.
    # TODO: If it's not a number, do it again.
    while True:
        raw_input = input("Choose> ")
        try:
            num = int(raw_input)
            return num
        except ValueError:
            print("Please enter a number instead.")


def find_next_page_from_choice(from_page, choice_number):
    # TODO: The magic stuff.
    # TODO: Return the page number of the page you get taken to by that choice.
    if from_page == 0:
        if choice_number == 0:
            return 1
    elif from_page == 1:
        if choice_number == 0:
            return 0
    else:
        return from_page


def run_game():
    current_page = 0
    while True:
        print_out_current_page(current_page)
        choice = get_integer_from_player()
        current_page = find_next_page_from_choice(current_page, choice)


run_game()


# THAT'S ALL FOLKS!

