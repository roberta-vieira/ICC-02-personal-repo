#!/bin/python

menu_1 = "1)Read and display names"
menu_2 = "2)Add a name"
menu_3 = "3)Exit"

user_menu_option = 0

while user_menu_option != 3:
    print("\n------------------------")
    print("Menu:")
    print(menu_1 + "\n" + menu_2 + "\n" + menu_3)
    user_menu_option = input("Please choose a menu option: ")

    if user_menu_option == '1':
        print("\n------------------------")
        print("Menu option:\n", menu_1)
        print("\nThis is the current file:")
        with open("names.txt", "r") as file:
            content = file.read()
            print(content)
            file.close()

    elif user_menu_option == '2':
        print("\n------------------------")
        print("Menu option:\n", menu_2)
        with open("names.txt", "a") as file:
            user_input = input("\nPlease write the name you wish add in the file: ")
            file.write(user_input + "\n")
            file.close()

    elif user_menu_option == '3':
        print("\n------------------------")
        print("Menu option:\n", menu_3)
        break
        
    else:
        print("\n\nWARNING: It seems you did not choose an available option, please select an option from 1 to 3.")
        

print("\nThank you for your visit!")