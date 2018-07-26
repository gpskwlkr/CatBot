import sqlite3
from random import shuffle, randint

class database:
    def __init__(self):
        self.connection = sqlite3.connect('phrases.db')
        self.cursor = self.connection.cursor()
        self.greeting = [g for row in self.cursor.execute("SELECT DISTINCT greetings FROM phrases") for g in row if len(g) > 1]
        self.cat_phrases = [c for row in self.cursor.execute("SELECT DISTINCT cat FROM phrases") for c in row if len(c) > 1]
        shuffle(self.greeting)
        shuffle(self.cat_phrases)

    def phrase(self, command):
        index = randint(0, len(self.greeting))
        while True:
            if index > 3:
                index = randint(0, len(self.greeting))
            else:
                break
        if command == "start":
            return self.greeting[index]
        else:
            return self.cat_phrases[index]

d = database()