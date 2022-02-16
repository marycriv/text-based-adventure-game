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
        # game_functions.reset_console()
        game_functions.format_print("Next chapter function")
        chapter_two = ChapterTwo()
        chapter_two.scene_one()

    def use_medkit(self):
        if "medkit" in hero.items:
            hero.items.remove("medkit")
            game_functions.format_print("You used your medkit")
            hero.health = 100
            print(f"\nHealth: {hero.health}")
        else: 
            game_functions.format_print("You don't have a medkit.")

    def handle_goblin(self): 
        goblin.move()
        if hero.location == goblin.location:
            goblin.talk()

    def random_medkit(self):
        medkit_find = random.choice([True, False])
        medkit_find = False # for testing purposes
        if medkit_find == True:
            hero.items.append("medkit")
            game_functions.format_print("You found a medkit!", 2)
            print("Enter 'm' to use it!")

    def random_bat_attack(self):
        bat_attack = random.choice([True, False])
        bat_attack = False # for testing purposes
        if bat_attack == True:
            game_functions.format_print("You were attacked by a bat", 2)
            hero.health -= random.randint(1,100)
            print(f"\nHealth: {hero.health}")
            if hero.health == 0:
                game_functions.format_print("You are dead!", 2)
                game_functions.handle_game_over()

    def scene_one(self):
        hero.location = "gate"
        game_functions.format_print(dialogue["one"][0])
        game_functions.format_print(dialogue["one"][1])
        game_functions.format_print(dialogue["options"][0])
        action = ""
        while action != "yes" or action != "no" or action != "m": 
            action = input("\n> ")
            if action == "yes": 
                self.scene_two()
            elif action == "no":
                game_functions.format_print(dialogue["one"][2])
            elif action == "m": 
                self.use_medkit()
            else: 
                game_functions.format_print(dialogue["one"][3])

    def scene_two(self):
        hero.location = "faerie"
        game_functions.format_print(dialogue["two"][0])
        game_functions.format_print(dialogue["two"][1])
        game_functions.format_print(dialogue["options"][0])
        action = ""
        while action != "yes" or action != "no" or action != "m": 
            action = input("\n> ")
            if action == "yes": 
                self.scene_three()
            elif action == "no":
                game_functions.format_print(dialogue["two"][2]) 
            elif action == "m": 
                self.use_medkit()
            else: 
                game_functions.format_print(dialogue["two"][3])

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
            elif action == "m": 
                self.use_medkit()
            else: 
                game_functions.format_print(dialogue["three"][3])

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
            elif action == "m": 
                self.use_medkit()
            else: 
                game_functions.format_print(dialogue["four"][5])