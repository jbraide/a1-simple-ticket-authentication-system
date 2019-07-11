from string import ascii_letters, punctuation, digits
from random import choice, randint


def usernameGenerator():
    min = 10
    max = 10

    string_format = ascii_letters
    generate_username = ''.join(choice(string_format)
                                for x in range(randint(min, max)))

    return generate_username


def passwordGenerator():
    min = 9
    max = 13

    string_format = ascii_letters
    generate_password = ''.join(choice(string_format)
                                for x in range(randint(min, max)))
    return generate_password
