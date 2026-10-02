import os
from engine import menu, mood_menu, mood_type, genre_type, mood_song, genre_song, read_inventory
def clear_terminal():
  os.system('cls' if os.name == 'nt' else 'clear')

clear_terminal()
print("-" * 40)
print("\n")
print("           WELCOME TO SPOTIFY MINI\n\n")
print("-" * 40)
print("-")

next = input("click 'ENTER' to continue....")
while next != "":
    print("")
    print("wrong input. Please click 'ENTER' to continue...")
    print("")
    next = input("Click 'ENTER' to continue...")

clear_terminal()

print("-" * 40)
print("        Select Your Preference\n")
print("               1. Mood")
print("               2. Genre")
print("           3. Your Playlist")
print("               4. Exit\n")
print("-"*40)
print("")

correct_input = False
while correct_input == False:
    choice = input("(1/2/3/4): ")
    if choice == "1":
        clear_terminal()
        print("What's Your Mood Right Now?\n")
        mood_type()
        print("")
        mood_song()
        correct_input = True
    elif choice == "2":
        clear_terminal()
        print("Any Genre You Like?\n")
        genre_type()
        print("")
        genre_song()
        correct_input = True
    elif choice == "3":
        clear_terminal()
        print("Your Playlist:\n")
        files = open("playlist.txt", "r")
        display = files.readlines()
        for i in display:
            print(f"- {i}")
        files.close()
        correct_input=True

    elif choice == "4":
        correct_input = True
    else:
        clear_terminal()
        print("-" * 40)
        print("        Select Your Preference\n")
        print("               1. Mood")
        print("               2. Genre")
        print("           3. Your Playlist")
        print("               4. Exit\n")
        print("-"*40)
        print("")
        print("Invalid choice. Please choose '1', '2', '3', or '4'.")

print("\n\n")
next = input("Click 'ENTER' to continue...")
while next != "":
    print("")
    print("wrong input. Please click 'ENTER' to continue...")
    print("")
    next = input("Click 'ENTER' to continue...")

clear_terminal()

print("-" * 40)
print("\n")
print("        THANK YOU FOR YOUR TIME!\n\n")
print("")
print("restart the code to continue with MINI SPOTIFY")
print("-"*40)
print("")

next = input("Click 'ENTER' to continue...")
while next != "":
    print("")
    print("wrong input. Please click 'ENTER' to continue...")
    print("")
    next = input("Click 'ENTER' to continue...")

clear_terminal()
