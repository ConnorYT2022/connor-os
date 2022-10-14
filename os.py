import os
import time

# Говно идея от коннора
# Connor os 2022.0.1

while (0 in range(5)):
    os.system("cls")
    print("-----------ConnorOS------------")
    command = input("Enter a command:")

    if command == "cmd":
        print("Opening CMD")
        time.sleep(5)
        os.system("start cmd")

    if command == "exit":
        print("Goodbye! (If program is not closing try enter command in range 4)")
        time.sleep(5)
        os.close
    
    if command == "developers":
        print("ConnorOS Creators")
        print("Connor (Dmytriev Lev Andreevich) - Head creator")
    
    else:
        print("I don't know this command!")
        time.sleep(5)
