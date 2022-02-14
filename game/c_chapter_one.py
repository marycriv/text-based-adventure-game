import sys
import random

from b_title import *

json_file_path = './dialogue.json'

with open(json_file_path, 'r') as j:
     contents = json.loads(j.read())

title_dialogue = contents["chapters"][1]["scenes"]

class ChapterOne:

    def next_chapter(self):
        print("continuing")

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
        medkit_find = True # for testing purposes
        if medkit_find == True:
            hero.items.append("medkit")
            game_functions.format_print("You found a medkit!", 2)
            print("Enter 'm' to use it!")

    def random_bat_attack(self):
        bat_attack = random.choice([True, False])
        bat_attack = True # for testing purposes
        if bat_attack == True:
            game_functions.format_print("You were attacked by a bat", 2)
            hero.health -= random.randint(1,100)
            print(f"\nHealth: {hero.health}")
            if hero.health == 0:
                game_functions.format_print("You are dead!", 2)
                game_functions.handle_game_over()

    def scene_one(self):
        hero.location = "entry"
        game_functions.format_print("Your name is Sarah Williams. You are a teenage girl.")
        self.random_medkit()
        self.handle_goblin()
        print("Ahead you can see a cavern. Will you continue?\n")
        print("Enter yes or no.")
        while True: 
            action = input("\n> ")
            if action == "yes": 
                self.scene_two()
            elif action == "no":
                game_functions.format_print("Water is dripping from the ceiling.") 
            elif action == "m": 
                self.use_medkit()
            else: 
                game_functions.format_print("You sit in total darkness, wondering if there is a way out.")

    def scene_two(self):
        hero.location = "cavern"
        self.random_bat_attack()
        self.handle_goblin()
        game_functions.format_print("You stumble into a dimly lit cavern.", 2)
        print("You cannot go right or left, but the cave continues ahead. Will you go on?")
        while True: 
            action = input("\n> ")
            if action == "yes": 
                self.scene_three()
            elif action == "no":
                game_functions.format_print("You sit down and eat a burrito.") 
            elif action == "m": 
                self.use_medkit()
            else: 
                game_functions.format_print("I do not understand your accent.")

    def scene_three(self):
        hero.location = "hallway"
        game_functions.format_print("You are in a wide hallway. It continues on indefinitely.", 2)
        self.handle_goblin()
        print("There's no turning back now. Will you go on?")
        while True: 
            action = input("\n> ")
            if action == "yes": 
                self.scene_four()
            elif action == "no":
                game_functions.format_print("You try to call for help, but no one is there.") 
            elif action == "m": 
                self.use_medkit()
            else: 
                game_functions.format_print("You wonder what time it is.")

    def scene_four(self):
        hero.location = "pit"
        game_functions.format_print("You fall headfirst into an ominous pit.", 2)
        game_functions.format_print("Luckily you only landed on your back.", 2)
        print("You can try to climb out. Will you try?")
        while True: 
            action = input("\n> ")
            if action == "yes": 
                game_functions.format_print("You try to climb out, but you slide off of the rocky walls.")
                self.next_chapter()
            elif action == "no":
                game_functions.format_print("You sit in utter darkness.") 
            elif action == "m": 
                self.use_medkit()
            else: 
                game_functions.format_print("You feel hopeless.")