import json
import re
from typing import List, Dict


def filter_users_by_age(age: int) -> None:
    """
    Filters users by age and prints the matching users.

    :param age: The age to filter users by.
    """
    with open("users.json", "r") as file:
        users: List[Dict] = json.load(file)

    filtered_users = [user for user in users if user["age"] == age]

    for user in filtered_users:
        print(user)


def filter_users_by_name(name: str) -> None:
    """
    Filters users by name (case-insensitive) and prints the matching users.

    :param name: The name to filter users by.
    """
    with open("users.json", "r") as file:
        users: List[Dict] = json.load(file)

    filtered_users = [user for user in users if user["name"].lower() == name.lower()]

    for user in filtered_users:
        print(user)


def filter_users_by_email(email: str) -> None:
    """
    Filters users by email (case-insensitive) and prints the matching users.

    :param email: The email to filter users by.
    """
    with open("users.json", "r") as file:
        users: List[Dict] = json.load(file)

    filtered_users = [user for user in users if user["email"].lower() == email.lower()]

    for user in filtered_users:
        print(user)


def is_valid_email(email: str) -> bool:
    """
    Validates whether the given string is a valid email address.

    :param email: The email string to validate.
    :return: True if valid, False otherwise.
    """
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None


if __name__ == "__main__":
    filter_option = input(
        "What would you like to filter by? (name, age, or email): "
    ).strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)

    elif filter_option == "age":
        while True:
            age_to_search = input("Enter an age to filter users: ").strip()
            try:
                age_int = int(age_to_search)
                filter_users_by_age(age_int)
                break
            except ValueError:
                print("Please enter a valid number.")

    elif filter_option == "email":
        while True:
            email_to_search = input("Enter an email to filter users: ").strip()
            if is_valid_email(email_to_search):
                filter_users_by_email(email_to_search)
                break
            else:
                print("Please enter a valid email address.")
    else:
        print("Filtering by that option is not yet supported.")
