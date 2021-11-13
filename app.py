from notion.client import NotionClient
import os

secret_code = open("config.txt", 'r').read()

client = NotionClient(token_v2=secret_code)

# Replace this URL with the URL of the page you want to edit
title = client.get_block("https://www.notion.so/simplesenpai/test-page-for-notion-python-6c9097ffa4c147e2a3ef3afc43a779d9")
content = client.get_block("https://www.notion.so/simplesenpai/test-page-for-notion-python-6c9097ffa4c147e2a3ef3afc43a779d9#2f8be5503d9b4e108cebd76d43f558cb")


print("Welcome to NotionPy!")

print("Current Editing Page:", title)

choice = ""

while choice.lower() != "exit":
    choice = input("What would you like to do? (Type 'help' for a list of commands) ")
    if choice.lower() == "help":
        print("Here are the commands you can use:")
        print("title read/change - Reads / changes the title of the working page!")
        print("content read/change - Reads / changes the content of the working page!")
        print("exit - Exits the program!")
    elif choice.lower() == "title read":
        print("The title of the page is:", title)
    elif choice.lower() == "title change":
        new_title = input("What would you like to change the title to? ")
        title = new_title
    elif choice.lower() == "content read":
        print("The content of the page is:", content)
    elif choice.lower() == "content change":
        new_content = input("What would you like to change the content to? ")
        content = new_content
    elif choice.lower() == "exit":
        print("Exiting the program...")
        break
    else:
        print("Invalid command!")