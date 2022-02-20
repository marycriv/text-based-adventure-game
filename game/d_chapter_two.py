import sys
import os
import climage

from b_title import *

json_file_path = './dialogue.json'

# with open(json_file_path, 'r') as j:
#      contents = json.loads(j.read())

# title_dialogue = contents["chapters"][2]["scenes"]

class ChapterTwo:

  def prologue(self):
    print("\n")
    os.system('cls||clear')
    game_functions.typewriter_print("CHAPTER TWO")
    owl = climage.convert('./assets/logo.jpeg', is_unicode=True)
    print(owl) 
    self.scene_one()

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
    print("chapter two")