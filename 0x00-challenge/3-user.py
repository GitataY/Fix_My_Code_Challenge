#!/usr/bin/python3
""" User class
"""


class User:
    """ User class """

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def is_valid_password(self, test_password):
        """ Validate the user's password """
        return self.password == test_password


if __name__ == '__main__':
    user = User("Test User", "SecretPassword")

    # Test case 1: Correct password
    test_password = "SecretPassword"
    if user.is_valid_password(test_password):
        print("Test case 1 passed")
    else:
        print("Test case 1 failed")

    # Test case 2: Incorrect password
    test_password = "WrongPassword"
    if user.is_valid_password(test_password):
        print("Test case 2 failed")
    else:
        print("Test case 2 passed")
