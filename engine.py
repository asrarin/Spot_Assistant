import os

class menu:
    def __init__(self):
        self.mood = False
        self. genre = False
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
