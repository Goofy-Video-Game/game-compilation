# Imports
import time

"""
    Just a bunch of random small games or just useful stuff.
    Copy to PyCharm and commit to GitHub at some point.
    validate the hell out of functions with try except when i can be bothered. 
    rename file to games.
    get ai to comply with pep 8 - DONT LET IT CHANGE LOGIC.
"""


def validate_alphabetical(word_to_validate, question):
    while not word_to_validate.isalpha():
        word_to_validate = input(f"re{question}")  # to work use 'enter' at beggining of prompt
    return word_to_validate


def validate_numerical(word_to_validate, question):
    while not word_to_validate.isdigit():
        word_to_validate = input(f"re{question}")  # to work use 'enter' at beggining of prompt
    return word_to_validate


"""
                      ^
Validation functions  |
                      |
"""


def talk_to_a_person():
    class People:
        humans = "yes"

        def __init__(self, name, age):
            self.name = name
            self.age = age

        def __str__(self):
            return (
                f"\nhello i am {self.name} i am {self.age} and if you were to ask me "
                f"if i was a human id say {self.humans}\n"
            )  # message for the people to say

    class Aliens(People):  # child class for aliens also displays message above
        humans = "no"

    # Making the people
    jamal = People("jamal", 34)
    jimbob = Aliens("jimbob of the planet blurbal", 21)

    # Asking who to talk to + validate
    while True:
        whos_talking = input("\ndo you want to hear jamal or jimbob speak? (case sensitive)\n").lower()
        if whos_talking == "jamal" or whos_talking == "jimbob":
            break
        else:
            print("you either did not enter or you misspelt one of the names. try again \n")

    if whos_talking == "jamal":
        return jamal
    else:
        return jimbob


def caesar_cipher():
    # Finds word to encrypt
    question_word = "enter a english word to create a caesar cipher of:\n"
    message_to_encrypt = input(question_word)
    check_against = message_to_encrypt.replace(" ", "")
    message_to_encrypt = validate_alphabetical(check_against, question_word)

    # Finds value to encrypt with
    question_number = "enter how many ascii values to change the number by\n"
    value_to_shift_by = input(question_number)
    value_to_shift_by = validate_numerical(value_to_shift_by, question_number)

    # Encrypts then prints value
    message = ""
    for j in range(len(message_to_encrypt)):
        ascii_value_word = ord(message_to_encrypt[j]) + int(value_to_shift_by)
        if ascii_value_word is not None:
            message += chr(ascii_value_word)
    return message


def fibonacci_sequence():
    # Gets what value to stop Fibonacci sequence at
    question = "\nenter the number where u want to fibonacci sequence to stop\n"
    where_to_end = input(question)
    validate_numerical(where_to_end, question)

    # Fibonacci sequence values
    a = 0  # first number
    b = 1  # second number
    c = 0  # addition of both prior numbers
    counter = 0  # counter

    # Prints Fibonacci sequence until number exceeds user entered limit
    print("\n0 this is the 1st value in the fibonacci sequence\n1 this is the 2nd value in the fibonacci sequence")

    # Finds next value then displays stops at user entered value
    while True:
        counter += 1
        time.sleep(0.1)
        c = a + b

        if c >= int(where_to_end):
            break

        a = b
        b = c
        print(f"{c:,} this is the {counter + 2}th value in the fibonacci sequence")
    return ""


def fizzbuzz():
    fizz_q = "please enter the first number (1-25)\n"
    buzz_q = "please enter the second number (1-25) Not the same as number 1\n"
    fizz = input(fizz_q)
    validate_numerical(fizz, fizz_q)

    buzz = input(buzz_q)
    return "worked"


"""
                                   ^                           
Actual like user-chosen functions  |
                                   |
"""

