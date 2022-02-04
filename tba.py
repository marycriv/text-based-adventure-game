# a text based adventure game

import sys
import os
import random
import time

import climage

class Game: 
    def typewriter_print(self, str, delay = 0.1):
        for letter in str:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(delay)
        print("\n")

    def format_print(self, str, delay = 0):
        print("\n" + str)
        time.sleep(delay)

    def reset_console(self):
        print("\n")
        os.system('cls||clear')

game_functions = Game()

class player:
    def __init__(self, location, health, items):
        self.location = location
        self.health = health
        self.items = items

hero = player("", 100, [])

class NPC: 
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def talk(self):
        game_functions.format_print(f"A {self.name} emerges from the shadows.")
        game_functions.format_print("'Charging into a goblin's nest! How dare you!'")
    
    def move(self):
        available_locations = ["entry", "cavern", "hallway", "pit"]
        self.location = random.choice(available_locations)

goblin = NPC("goblin", "hallway")

class World:

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

    def handle_game_over(self):
        game_functions.typewriter_print("GAME OVER")
        sys.exit()

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
                self.handle_game_over()

    def chapter_one(self):
        # output = climage.convert('./assets/logo.jpeg', is_unicode=True)
        # print(output)
        escher = climage.convert('./assets/maze.jpeg', is_unicode=True)
        print(escher)
        # self.scene_one()

    def scene_one(self):
        game_functions.reset_console()
        hero.location = "entry"
        game_functions.format_print("You are in a dark cave. The entry has been sealed by fallen rocks. There is no way out.")
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
                self.handle_game_over()
            elif action == "no":
                game_functions.format_print("You sit in utter darkness.") 
            elif action == "m": 
                self.use_medkit()
            else: 
                game_functions.format_print("You feel hopeless.")


# chapter one
new_world = World()
new_world.chapter_one()