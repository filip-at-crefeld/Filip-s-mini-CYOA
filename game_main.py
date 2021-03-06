"""Filip's version of a basic CYOA"""

import random


def print_out_current_page(page_number):
    # TODO: Print to the console the text from that page. Include the choices like 1) xxx 2) xxx.

    # Are we on page 0?
    if page_number == 0:

        # Print out stuff on page 0
        print("=== Page zero ===\nStory?\n0) Go to Page 1.\n1) Skip to Page 2.")

    # Are we on page 1?
    elif page_number == 1:

        # Print out stuff on page 1
        print("=== Page one ===\nMiddle?\n0) Go back to 0.\n1) On to 2.")

    # Are we on page 2?
    elif page_number == 2:

        # Print out stuff on page 2
        print("=== Page two ===\nEnd-ness?\n0) Start over on Page 0.")


def get_integer_from_player():
    # TODO: Use input function to get a string, make sure it's a number, then return an int.
    # TODO: If it's not a number, do it again.

    # An infinite loop
    while True:

        # Asks for an input and then assigns the string of that to raw_input
        raw_input = input("Choose> ")

        # Marks the start of an error-catching section
        try:

            # Turn the string into an integer // THIS STATEMENT IS RISKY
            num = int(raw_input)

            # Exit out of the function here. ESCAPE!
            return num

        # Ends the error catching section, starts the error handling section
        except ValueError:

            # "Handle" the error by reporting to the player
            print("Please enter a number instead.")

        # This is the end of the while loop, so if you get here start the next loop


def find_next_page_from_choice(from_page, choice_number):
    # TODO: The magic stuff.
    # TODO: Return the page number of the page you get taken to by that choice.

    # This method is made up of two layers of if-statements.
    # Outer layer: identify which page we're making choices on.
    # Inner layer: identify which numbered choice was submitted.
    # Success? Then return the new page number.
    # Fail?    Then return the original page number. (So don't change things.)
    if from_page == 0:
        if choice_number == 0:
            return 1
        elif choice_number == 1:
            return 2


    elif from_page == 1:
        if choice_number == 0:
            return 0
        elif choice_number == 1:
            return 2


    elif from_page == 2:
        if choice_number == 0:
            return 0


    elif from_page == 3:
        if choice_number == 0:
            result = random.randint(0, 1)
            if result == 0:
                print("You won!")
            else:
                print("You lost")


    print("Invalid choice for this page!\nRepeating the page.")
    return from_page


def run_game():
    current_page = 0
    while True:
        print_out_current_page(current_page)
        choice = get_integer_from_player()
        current_page = find_next_page_from_choice(current_page, choice)


run_game()


# THAT'S ALL FOLKS!

