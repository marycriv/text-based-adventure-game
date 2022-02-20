import sys
import random

from b_title import *
from d_chapter_two import *

json_file_path = './dialogue.json'

with open(json_file_path, 'r') as j:
     contents = json.loads(j.read())

dialogue = contents["chapters"][1]["scenes"]

class ChapterOne:

    def next_chapter(self):
        game_functions.format_print("Next chapter function")
        chapter_two = ChapterTwo()
        chapter_two.scene_one()

    def give_ring(self):
        if "ring" in hero.items:
            hero.items.remove("ring")
            game_functions.format_print("You give the goblin your ring.")
        else: 
            game_functions.format_print("You don't have a ring.")

    def scene_one(self):
        hero.location = "gate"
        game_functions.format_print(dialogue["one"][0])
        game_functions.format_print(dialogue["one"][1])
        game_functions.format_print(dialogue["one"][2])
        game_functions.format_print(dialogue["one"][3])
        game_functions.format_print(dialogue["options"][1])
        # action = input("\n> ")
        action = ""
        while action != "yes" or action != "no" or action != "m": 
            action = input("\n> ")
            if action == "yes": 
                self.give_ring()
                self.scene_two()
            elif action == "no":
                game_functions.format_print(dialogue["one"][4])
            else: 
                game_functions.format_print(dialogue["options"][0])

    def scene_two(self):
        hero.location = "faerie"
        game_functions.format_print(dialogue["two"][0])
        game_functions.format_print(dialogue["two"][1])
        game_functions.format_print(dialogue["options"][1])
        action = ""
        while action != "yes" or action != "no" or action != "m": 
            action = input("\n> ")
            if action == "yes": 
                self.scene_three()
            elif action == "no":
                game_functions.format_print(dialogue["two"][2]) 
            else: 
                game_functions.format_print(dialogue["options"][1])

    def scene_three(self):
        hero.location = "corridor"
        game_functions.format_print(dialogue["three"][0])
        game_functions.format_print(dialogue["three"][1])
        action = ""
        while action != "yes" or action != "no" or action != "m": 
            action = input("\n> ")
            if action == "yes": 
                self.scene_four()
            elif action == "no":
                game_functions.format_print(dialogue["three"][2]) 
            else: 
                game_functions.format_print(dialogue["options"][1])

    def scene_four(self):
        hero.location = "worm"
        game_functions.format_print(dialogue["four"][0])
        game_functions.format_print(dialogue["four"][1])
        game_functions.format_print(dialogue["four"][2])
        action = ""
        while action != "yes" or action != "no" or action != "m": 
            action = input("\n> ")
            if action == "yes": 
                game_functions.format_print(dialogue["four"][3])
                self.next_chapter()
            elif action == "no":
                game_functions.format_print(dialogue["four"][4]) 
            else: 
                game_functions.format_print(dialogue["options"][1])