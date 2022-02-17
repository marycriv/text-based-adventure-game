import os
import time
import sys
import random

import json

import climage
from playsound import playsound

json_file_path = './dialogue.json'

with open(json_file_path, 'r') as j:
     contents = json.loads(j.read())

title_dialogue = contents["chapters"][0]["scenes"]

class Game: 
    def typewriter_print(self, str, delay = 0.1):
        for letter in str:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(delay)
        print("\n")

    def format_print(self, str, delay = 0):
        print("\n" + str + "\n")
        time.sleep(delay)

    def reset_console(self):
        print("\n")
        os.system('cls||clear')

    def handle_game_over(self):
        print("GAME OVER")
        sys.exit()

game_functions = Game()

class player:
    def __init__(self, firstname, lastname, location, health, items):
        self.firstname = firstname
        self.lastname = lastname
        self.location = location
        self.health = health
        self.items = items

hero = player("Sarah", "Williams", "", 100, ["ring", "lipstick"])

class NPC: 
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def talk(self):
        game_functions.format_print(f"A {self.name} emerges from the shadows.")
        game_functions.format_print("'Charging into a goblin's nest! How dare you!'")
    
    def move(self):
        available_locations = ["gate", "faerie", "corridor", "worm"]
        self.location = random.choice(available_locations)

goblin = NPC("goblin", "hallway")

class Title:

  def title_card(self):
    game_functions.reset_console()
    # playsound('./assets/soundtrack/openingtitlesunderground.m4a', False)
    game_functions.typewriter_print(title_dialogue["one"][0])
    game_functions.typewriter_print(title_dialogue["one"][1])
    # owl = climage.convert('./assets/2.png', is_unicode=True)
    # print(owl)
    game_functions.format_print(title_dialogue["one"][2])