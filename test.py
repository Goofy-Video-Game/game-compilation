import functions as ff

def main():

    # Dictionary of functions
    functionscall = {
        "talk to a person":ff.talk_to_a_person,
        "caesar cipher": ff.caesar_cipher,
        "fibonacci sequence": ff.fibonacci_sequence,
        "fizzbuzz": ff.fizzbuzz,
    }

    # Asks what function to run then runs it
    chosen_function = input(
        "enter one of the following (case sensitive):\n"
        "  'talk to a person'\n"
        "  'caesar cipher'\n"
        "  'fibonacci sequence'\n"
        "  'fizzbuzz'\n\n"
    ).lower()

    if chosen_function in functionscall:
        print(functionscall[chosen_function]())


if __name__ == "__main__":
    main()