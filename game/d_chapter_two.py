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
  
  def scene_one(self):
    print("chapter two")