import os
def clear_terminal():
  os.system('cls' if os.name == 'nt' else 'clear')

class menu:
    def __init__(self):
        self.mood = False
        self.genre = False
        self.playlist_total = False
        self.exit =False

    def mood(self):
        self.mood = True
        print("Mood Selected")

    def genre(self):
        self.genre = True

    def playlist_total(self):
        self.playlist_total = True

    def exit(self):
        self.exit = True



class mood_menu():
    def __init__(self, mood_selection):
        self.mood_selection = mood_selection

    def __str__(self):
        return f"{self.mood_selection}"

class genre_menu():
    def __init__(self, genre_selection):
        self.genre_selection = genre_selection

    def __str__(self):
        return f"{self.genre_selection}"

mood_list = [
    mood_menu("1. Upbeat/Happy"),
    mood_menu("2. Chill/Relaxed"),
    mood_menu("3. Hyped/Energetic"),
    mood_menu("4. Sad/Melancholic"),
    mood_menu("5. Focused/Calm")
]

def mood_type():
    for mood in mood_list:
        print(mood)

def mood_song():
    correct_input = False
    while correct_input == False:
        choice = input("(1/2/3/4/5): ")
        if choice == "1":
            clear_terminal()
            print("Upbeat/Happy\n")
            print("")
            print("1. Espresso by Sabrina Carpenter\n2. Happy by Pharrell Williams\n3. Can’t Stop the Feeling! by Justin Timberlake\n4. Uptown Funk by Mark Ronson ft. Bruno Mars\n5. Dynamite by BTS\n6. Levitating by Dua Lipa\n7. Good Time by Owl City & Carly Rae Jepsen\n8. Shut Up and Dance by WALK THE MOON\n9. Shake It Off by Taylor Swift\n10. I Gotta Feeling by Black Eyed Peas\n")
            print("")
            while correct_input == False:
                choice = input("Do you wish to add this to your playlist?(yes/no): ").lower()
                if choice == "yes":
                    clear_terminal()
                    print("Songs Successfully Added to Your Playlist")
                    update_inventory("Espresso by Sabrina Carpenter\nHappy by Pharrell Williams\nCan’t Stop the Feeling! by Justin Timberlake\nUptown Funk by Mark Ronson ft. Bruno Mars\nDynamite by BTS\nLevitating by Dua Lipa\nGood Time by Owl City & Carly Rae Jepsen\nShut Up and Dance by WALK THE MOON\nShake It Off by Taylor Swift\nI Gotta Feeling by Black Eyed Peas")
                    correct_input = True
                elif choice == "no":
                    clear_terminal()
                    print("Songs Unsuccessfully Added to Your Playlist")
                    correct_input = True
                else:
                    clear_terminal()
                    print("Do you wish to add this to your playlist?:\n")
                    print("")
                    mood_type()
                    print("")
                    print("Invalid choice. Please choose 'yes', or 'no'.")

        elif choice == "2":
            clear_terminal()
            print("Chill / Relaxed\n")
            print("")
            print("1. Feather by Sabrina Carpenter\n2. Sunflower by Post Malone & Swae Lee\n3. Sunday Morning by Maroon 5\n4. Location by Khalid\n5. Double Take by dhruv\n6.Best Part by Daniel Caesar ft. H.E.R.\n7. Until I Found You by Stephen Sanchez\n8. Peaches by Justin Bieber ft. Daniel Caesar & Giveon\n9. Put Your Records On by Corinne Bailey Rae\n10. Riptide by Vance Joy\n")
            print("")
            while correct_input == False:
                choice = input("Do you wish to add this to your playlist?(yes/no): ").lower()
                if choice == "yes":
                    clear_terminal()
                    print("Songs Successfully Added to Your Playlist")
                    update_inventory("Feather by Sabrina Carpenter\nSunflower by Post Malone & Swae Lee\nSunday Morning by Maroon 5\nLocation by Khalid\nDouble Take by dhruv\nBest Part by Daniel Caesar ft. H.E.R.\nUntil I Found You by Stephen Sanchez\nPeaches by Justin Bieber ft. Daniel Caesar & Giveon\nPut Your Records On by Corinne Bailey Rae\nRiptide by Vance Joy")
                    correct_input = True
                elif choice == "no":
                    clear_terminal()
                    print("Songs Unsuccessfully Added to Your Playlist")
                    correct_input = True
                else:
                    clear_terminal()
                    print("Do you wish to add this to your playlist?:\n")
                    print("")
                    mood_type()
                    print("")
                    print("Invalid choice. Please choose 'yes', or 'no'.")

        elif choice == "3":
            clear_terminal()
            print("Hyped / Energetic\n")
            print("")
            print("1. Please Please Please by Sabrina Carpenter\n2. Can’t Hold Us by Macklemore & Ryan Lewis\n3. Power by Kanye West\n4. Club Can’t Handle Me by Flo Rida ft. David Guetta\n5. Turn Down for What by DJ Snake & Lil Jon\n6. Eye of the Tiger by Survivor\n7. Believer by Imagine Dragons\n8. BANG BANG BANG by BIGBANG\n9. Till I Collapse by Eminem\n")
            print("")
            while correct_input == False:
                choice = input("Do you wish to add this to your playlist?(yes/no): ").lower()
                if choice == "yes":
                    clear_terminal()
                    print("Songs Successfully Added to Your Playlist")
                    update_inventory("Please Please Please by Sabrina Carpenter\nCan’t Hold Us by Macklemore & Ryan Lewis\nPower by Kanye West\nClub Can’t Handle Me by Flo Rida ft. David Guetta\nTurn Down for What by DJ Snake & Lil Jon\nEye of the Tiger by Survivor\nBeliever by Imagine Dragons\nBANG BANG BANG by BIGBANG\nTill I Collapse by Eminem")
                    correct_input = True
                elif choice == "no":
                    clear_terminal()
                    print("Songs Unsuccessfully Added to Your Playlist")
                    correct_input = True
                else:
                    clear_terminal()
                    print("Do you wish to add this to your playlist?:\n")
                    print("")
                    mood_type()
                    print("")
                    print("Invalid choice. Please choose 'yes', or 'no'.")
        elif choice == "4":
            clear_terminal()
            print("Sad/ Melancholic\n")
            print("")
            print("1. skinny dipping by Sabrina Carpenter\n2. Someone Like You by Adele\n3. Glimpse of Us by Joji\n4. Drivers License by Olivia Rodrigo\n5. Fix You by Coldplay\n6. All I Want by Kodaline\n7. Say Something by A Great Big World & Christina Aguilera\n8. When I Was Your Man by Bruno Mars\n9. The Night We Met by Lord Huron\n10. Heather by Conan Gray\n")
            print("")
            while correct_input == False:
                choice = input("Do you wish to add this to your playlist?(yes/no): ").lower()
                if choice == "yes":
                    clear_terminal()
                    print("Songs Successfully Added to Your Playlist")
                    update_inventory("skinny dipping by Sabrina Carpenter\nSomeone Like You by Adele\nGlimpse of Us by Joji\nDrivers License by Olivia Rodrigo\nFix You by Coldplay\nAll I Want by Kodaline\nSay Something by A Great Big World & Christina Aguilera\nWhen I Was Your Man by Bruno Mars\nThe Night We Met by Lord Huron\nHeather by Conan Gray")
                    correct_input = True
                elif choice == "no":
                    clear_terminal()
                    print("Songs Unsuccessfully Added to Your Playlist")
                    correct_input = True
                else:
                    clear_terminal()
                    print("Do you wish to add this to your playlist?:\n")
                    print("")
                    mood_type()
                    print("")
                    print("Invalid choice. Please choose 'yes', or 'no'.")
        elif choice == "5":
            clear_terminal()
            print("Focused/ Calm\n")
            print("")
            print("1. coincidence by Sabrina Carpenter\n2. Weightless by Marconi Union\n3. River Flows in You by Yiruma\n4. Nuvole Bianche by Ludovico Einaudi\n5. Experience by Ludovico Einaudi\n6. Cornfield Chase by Hans Zimmer\n7. Clair de Lune by Claude Debussy\n8. Gymnopédie No.1 by Erik Satie\n9. Sunset Lover by Petit Biscuit\n10. A Moment’s Peace by Aakash Gandhi\n")
            print("")
            while correct_input == False:
                choice = input("Do you wish to add this to your playlist?(yes/no): ").lower()
                if choice == "yes":
                    clear_terminal()
                    print("Songs Successfully Added to Your Playlist")
                    update_inventory("coincidence by Sabrina Carpenter\nWeightless by Marconi Union\nRiver Flows in You by Yiruma\nNuvole Bianche by Ludovico Einaudi\nExperience by Ludovico Einaudi\nCornfield Chase by Hans Zimmer\nClair de Lune by Claude Debussy\nGymnopédie No.1 by Erik Satie\nSunset Lover by Petit Biscuit\nA Moment’s Peace by Aakash Gandhi")
                    correct_input = True
                elif choice == "no":
                    clear_terminal()
                    print("Songs Unsuccessfully Added to Your Playlist")
                    correct_input = True
                else:
                    clear_terminal()
                    print("Do you wish to add this to your playlist?:\n")
                    print("")
                    mood_type()
                    print("")
                    print("Invalid choice. Please choose 'yes', or 'no'.")
        else:
            clear_terminal()
            print("What's Your Mood Right Now?\n")
            print("")
            mood_type()
            print("")
            print("Invalid choice. Please choose '1', '2', '3', '4', or '5'.")




genre_list = [
    genre_menu("1. Pop"),
    genre_menu("2. Hip-Hop/Rap"),
    genre_menu("3. Rock"),
    genre_menu("4. R&B/Soul"),
    genre_menu("5. Electronic/Dance(EDM)")
]

def genre_type():
    for genre in genre_list:
        print(genre)

def genre_song():
    correct_input = False
    while correct_input == False:
        choice = input("(1/2/3/4/5): ")
        if choice == "1":
            clear_terminal()
            print("Pop\n")
            print("")
            print("1. Taste by Sabrina Carpenter\n2. As It Was by Harry Styles\n3. Blinding Lights by The Weeknd\n4. Cruel Summer by Taylor Swift\n5. vampire by Olivia Rodrigo\n6. Levitating by Dua Lipa\n7. Shape of You by Ed Sheeran\n8. Greedy by Tate McRae\n9. Flowers by Miley Cyrus\n10. Water by Tyla\n")
            print("")
            while correct_input == False:
                choice = input("Do you wish to add this to your playlist?(yes/no): ").lower()
                if choice == "yes":
                    clear_terminal()
                    print("Songs Successfully Added to Your Playlist")
                    update_inventory("Taste by Sabrina Carpenter\nAs It Was by Harry Styles\nBlinding Lights by The Weeknd\nCruel Summer by Taylor Swift\nvampire by Olivia Rodrigo\nLevitating by Dua Lipa\nShape of You by Ed Sheeran\nGreedy by Tate McRae\nFlowers by Miley Cyrus\nWater by Tyla")
                    correct_input = True
                elif choice == "no":
                    clear_terminal()
                    print("Songs Unsuccessfully Added to Your Playlist")
                    correct_input = True
                else:
                    clear_terminal()
                    print("Do you wish to add this to your playlist?:\n")
                    print("")
                    mood_type()
                    print("")
                    print("Invalid choice. Please choose 'yes', or 'no'.")

        elif choice == "2":
            clear_terminal()
            print("Hip-Hop / Rap\n")
            print("")
            print("1. SICKO MODE by Travis Scott\n2. HUMBLE. by Kendrick Lamar\n3. God's Plan by Drake\n4. Lose Yourself by Eminem\n5. Not Like Us by Kendrick Lamar\n6. Rockstar by Post Malone ft. 21 Savage\n7. First Class by Jack Harlow\n8. N95 by Kendrick Lamar\n9. Industry Baby by Lil Nas X ft. Jack Harlow\n10. Old Town Road by Lil Nas X ft. Billy Ray Cyrus\n")
            print("")
            while correct_input == False:
                choice = input("Do you wish to add this to your playlist?(yes/no): ").lower()
                if choice == "yes":
                    clear_terminal()
                    print("Songs Successfully Added to Your Playlist")
                    update_inventory("SICKO MODE by Travis Scott\nHUMBLE. by Kendrick Lamar\nGod's Plan by Drake\nLose Yourself by Eminem\nNot Like Us by Kendrick Lamar\nRockstar by Post Malone ft. 21 Savage\nFirst Class by Jack Harlow\nN95 by Kendrick Lamar\nIndustry Baby by Lil Nas X ft. Jack Harlow\nOld Town Road by Lil Nas X ft. Billy Ray Cyrus")
                    correct_input = True
                elif choice == "no":
                    clear_terminal()
                    print("Songs Unsuccessfully Added to Your Playlist")
                    correct_input = True
                else:
                    clear_terminal()
                    print("Do you wish to add this to your playlist?:\n")
                    print("")
                    mood_type()
                    print("")
                    print("Invalid choice. Please choose 'yes', or 'no'.")

        elif choice == "3":
            clear_terminal()
            print("Rock\n")
            print("")
            print("1. Bohemian Rhapsody by Queen\n2. Smells Like Teen Spirit by Nirvana\n3. Hotel California by Eagles\n4. Sweet Child O' Mine by Guns N' Roses\n5. Numb by Linkin Park\n6. In the End by Linkin Park\n7. Seven Nation Army by The White Stripes\n8. Do I Wanna Know? by Arctic Monkeys\n9. Back In Black by AC/DC\n10. Demons by Imagine Dragons\n")
            print("")
            while correct_input == False:
                choice = input("Do you wish to add this to your playlist?(yes/no): ").lower()
                if choice == "yes":
                    clear_terminal()
                    print("Songs Successfully Added to Your Playlist")
                    update_inventory("Bohemian Rhapsody by Queen\nSmells Like Teen Spirit by Nirvana\nHotel California by Eagles\nSweet Child O' Mine by Guns N' Roses\nNumb by Linkin Park\nIn the End by Linkin Park\nSeven Nation Army by The White Stripes\nDo I Wanna Know? by Arctic Monkeys\nBack In Black by AC/DC\nDemons by Imagine Dragons")
                    correct_input = True
                elif choice == "no":
                    clear_terminal()
                    print("Songs Unsuccessfully Added to Your Playlist")
                    correct_input = True
                else:
                    clear_terminal()
                    print("Do you wish to add this to your playlist?:\n")
                    print("")
                    mood_type()
                    print("")
                    print("Invalid choice. Please choose 'yes', or 'no'.")
        elif choice == "4":
            clear_terminal()
            print("R&B/ Soul\n")
            print("")
            print("1. Die For You by The Weeknd\n2. Kill Bill by SZA\n3. Snooze by SZA\n4. Redbone by Childish Gambino\n5. Earned It by The Weeknd\n6. Get You by Daniel Caesar ft. Kali Uchis\n7. Adorn by Miguel\n8. Free Mind by Tems\n9. Under The Influence by Chris Brown\n10. CUFF IT by Beyoncé\n")
            print("")
            while correct_input == False:
                choice = input("Do you wish to add this to your playlist?(yes/no): ").lower()
                if choice == "yes":
                    clear_terminal()
                    print("Songs Successfully Added to Your Playlist")
                    update_inventory("Die For You by The Weeknd\nKill Bill by SZA\nSnooze by SZA\nRedbone by Childish Gambino\nEarned It by The Weeknd\nGet You by Daniel Caesar ft. Kali Uchis\nAdorn by Miguel\nFree Mind by Tems\nUnder The Influence by Chris Brown\nCUFF IT by Beyoncé")
                    correct_input = True
                elif choice == "no":
                    clear_terminal()
                    print("Songs Unsuccessfully Added to Your Playlist")
                    correct_input = True
                else:
                    clear_terminal()
                    print("Do you wish to add this to your playlist?:\n")
                    print("")
                    mood_type()
                    print("")
                    print("Invalid choice. Please choose 'yes', or 'no'.")
        elif choice == "5":
            clear_terminal()
            print("Electronic/ Dance (EDM)\n")
            print("")
            print("1. Closer by The Chainsmokers ft. Halsey\n2. Faded by Alan Walker\n3. Wake Me Up by Avicii\n4. Titanium by David Guetta ft. Sia\n5. Lean On by Major Lazer & DJ Snake ft. MØ\n6. Don't You Worry Child by Swedish House Mafia\n7. Stay by Zedd & Alessia Cara\n8. Animals by Martin Garrix\n9. Stargazing by Kygo ft. Justin Jesso\n10. One Kiss by Calvin Harris & Dua Lipa\n")
            print("")
            while correct_input == False:
                choice = input("Do you wish to add this to your playlist?(yes/no): ").lower()
                if choice == "yes":
                    clear_terminal()
                    print("Songs Successfully Added to Your Playlist")
                    update_inventory("Closer by The Chainsmokers ft. Halsey\Faded by Alan Walker\nWake Me Up by Avicii\nTitanium by David Guetta ft. Sia\nLean On by Major Lazer & DJ Snake ft. MØ\nDon't You Worry Child by Swedish House Mafia\nStay by Zedd & Alessia Cara\nAnimals by Martin Garrix\nStargazing by Kygo ft. Justin Jesso\nOne Kiss by Calvin Harris & Dua Lipa")
                    correct_input = True
                elif choice == "no":
                    clear_terminal()
                    print("Songs Unsuccessfully Added to Your Playlist")
                    correct_input = True
                else:
                    clear_terminal()
                    print("Do you wish to add this to your playlist?:\n")
                    print("")
                    mood_type()
                    print("")
                    print("Invalid choice. Please choose 'yes', or 'no'.")
        else:
            clear_terminal()
            print("Any Genre You Like?\n")
            genre_type()
            print("")
            print("Invalid choice. Please choose '1', '2', '3', '4', or '5'.")


def update_inventory(x):
    files = open("playlist.txt", "a")
    files.write(x + "\n")
    files.close()

def read_inventory():
    files = open("playlist.txt", "r")
    inventory = files.readlines()
    inventory = [item.strip() for item in inventory]
    return inventory
