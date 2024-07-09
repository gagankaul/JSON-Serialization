
# Online Python - IDE, Editor, Compiler, Interpreter

import json
import os

def read_user_data():
    try:
        with open('user_data.json', 'r') as file:
            user_list = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        user_list = []
    return user_list

def get_user_data():

    user_list = read_user_data()

    while True:
        user_data = {}
        user_data["name"] = input("Enter name: ")
        user_data["age"] = input("Enter age: ")
        user_data["city"] = input("Enter city: ")
        user_list.append(user_data)
        print("User Added Successfull!")

        choice = input("Add another user (y/n)?: ")
        if choice == "n":
            break
    with open('user_data.json', 'w') as file:
        json.dump(user_list, file)

    print(user_list)

def edit_user_data(name):
    if not os.path.exists('user_data.json'):
        print("No user data found.")
        return

    with open('user_data.json', 'r') as file:
        user_list = json.load(file)

    user_found = False
    for user_data in user_list:
        if user_data["name"].lower() == name.lower():
            user_data["age"] = input("Enter new age: ")
            user_data["city"] = input("Enter new city: ")
            print("User data updated successfully.")
            user_found = True
            break
    if not user_found:
        print("User not found.")

    with open('user_data.json', 'w') as file:
        json.dump(user_list, file)

    print("User data saved successfully!")
    print(user_list)

def delete_user_data(name):
    if not os.path.exists('user_data.json'):
        print("No user data found.")
        return

    with open('user_data.json', 'r') as file:
        user_list = json.load(file)

    user_found = False
    
    for user_data in user_list:
        if user_data["name"].lower() == name.lower():
            user_list.remove(user_data)
            print("User data deleted successfully.")
            user_found = True
            break
    if not user_found:
        print("User not found.")

    with open('user_data.json', 'w') as file:
        json.dump(user_list, file)

    print("User data saved successfully!")
    print(user_list)
    
edit_name = input("Enter name to edit: ")

#get_user_data()
#edit_user_data(edit_name)
delete_user_data(edit_name)
