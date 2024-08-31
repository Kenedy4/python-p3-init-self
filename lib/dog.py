#!/usr/bin/env python3

class Dog:
    bark_sound = "Woof!"

    def __init__(self, name="Unnamed", breed="Mutt"):
        self.name = name
        self.breed = breed

    def sit(self):
        print("The dog is sitting.")

    def bark(self):
        print(self.bark_sound)