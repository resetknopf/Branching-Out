import json

def filter_users_by_age(age):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["age"] == age]

    for user in filtered_users:
        print(user)

def filter_users_by_name(name):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["name"].lower() == name.lower()]

    for user in filtered_users:
        print(user)

if __name__ == "__main__":
    filter_option = input(
        "What would you like to filter by? (Currently, only 'name' and 'age' are supported): ").strip().lower()

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
    else:
        print("Filtering by that option is not yet supported.")

