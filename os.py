import os
import time

# Говно идея от коннора
# Connor os 2022.0.3

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
    
    if command == "createdirectory":
        foldername = input("Enter a folder name: ")
        print("Creating directory, please wait.")
        time.sleep(5)
        os.mkdir(foldername)
        print("Folder created!")
    
    if command == "createfile":
        filename = input("Enter a file name: ")
        file = open(filename, "w")
        time.sleep(5)
        print("Created!")
    
    if command == "off":
        print("Твоему комплюхтеру пиздааа!")
        os.system("shutdown /s")
    
    if command == "offuser":
        print("Твоему юзеру пиздааа!")
        os.system("shutdown /l")
    
    if command == "reload":
        print("Твоему компу перезагрузка нужна!")
        os.system("shutdown /r")
    
    if command == "hibernation":
        print("Deleting you compluhter")
        os.system("shutdown /h")
    if command == "help":
        print("Opening a command list")
        os.system("start Txts/commands.txt")
    else:
        print("I don't know this command!")
        time.sleep(5)
