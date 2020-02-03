# -*- coding: utf-8 -*-

import json
from os import system
from getpass import getpass

""" 
  Este script permitira lo siguiente: 
  - Crear login (Usuario y contraseña)
  - A ese usuario se le permitira crear, eliminar y ocultar carpeta
      dandole roles, accediendo a tales permisos
"""
# ============================    VARIABLES   ============================== #
FILE = '.data.json'
DEFAULT = [
  {'name': 'test', 'password': 'test1234'},
  {'name': 'sample', 'password': 'sample321'}
]

# ============================    HELPERS   ============================== #
def main_message():
  print('')
  print('                RUNNING SCRIPT            ')
  print('')
  print('** MENU **')
  print('=============================================')
  print('Select an option:')
  print('')
  print('1) Login')
  print('2) Register')
  print('3) About')
  print('4) Help')
  print('')
  print('0) Exit')
  print('─────────────────────────────────────────────')

def login_message():
  print('')
  print('                PRIVATE FILES           ')
  print('')
  print('───> SCRIPT MENU ')
  print(f'{D_GRAY}============================================={END}')
  print('Select an option:')
  print('')
  print('1) Create Folder')
  print('2) Create File')
  print('3) Delete Folder')
  print('4) Delete File')
  print('')
  print('0) Exit')
  print(f'{D_GRAY}============================================={END}')

def clean(time=0):
  system(f'sleep {time} && clear')

def setDefault():
  try:
    with open(FILE, 'r+') as file:
      if not file.read():
        json.dump(DEFAULT, file, indent=2)

  except FileNotFoundError as notFound:
    # Create el file
    system(f'touch {FILE}')
    setDefault()

# =============================    COLORS   ================================ #
RED, WHITE, BLUE, CYAN, GREEN, END = '\033[91m', '\033[46m', '\033[34m', '\033[36m', '\033[1;32m', '\033[0m'
PURPLE = '\033[35m'
BLACK = '\033[30m'

#  Lights
L_CYAN   = '\033[1;36m'
L_BLUE   = '\033[1;34m'      
L_PURPLE = '\033[1;35m'
D_GRAY   = '\033[1;30m'
L_GREEN  = '\033[1;32m'

# =============================     MAIN    ================================ #

def main():
  isValid = False
  while True:
    try:
      main_message() if not isValid else login_message()
      option = int(input(f'{CYAN}>>> {END}'))

      if option == 1:
        entry = login()
        if entry:
          isValid = True

      elif option == 2:
        register() # Register

      elif option == 3:
        isValid = True # About

      elif option == 4:
        pass # Help

      elif option == 0:
        break
      
    except:
      print('Character invalid!')
      clean(.5)


# >>>>>>>>>>>>>>>>>>>>>>>> MAIN FUNCTIONS

def login():
  exist = False
  valid = None
  clean()

  try:
    with open(FILE) as file:
      user = input('Please! Enter your username: ')
      passwd = getpass(prompt='Please! enter your password: ')
      
      db = json.load(file)
      db_user = None
      db_passwd = None


      for x in range(0, len(db)):
        if user in db[x]['name']:
          exist = True
          db_user = db[x]['name']
          db_passwd = db[x]['password']
          break
        else:
          exist = False

      if exist:
        if db_passwd == passwd:
          print('Acceding')
          clean(1)
          return True

        else:
          print('Password isnt valid')

      else:
        print(f'{RED}ERROR: {END}{WHITE}This user doesnt exist{END}')

  except:
    print('Doesnt exists users!')
    clean(.5)

def register():
  temp_file = None
  exist = False
  try:
    # Read JSON
    with open(FILE) as file:
      name = input('Enter your new username: ')
      passwd = getpass(prompt='Enter your new password: ')
      confirm = getpass(prompt='Enter your password again: ')

      db = json.load(file)

      for x in range(0, len(db)):
        if name in db[x]['name']:
          exist = True
          break

        else:
          exist = False

      if exist:
        clean()
        print(f'{RED}ERROR: {END}{WHITE}This user already exist{END}')
        return(0)

      else:
        if passwd == confirm:
          newuser = {'name': name, 'password': passwd}
          db.append(newuser)
      
      temp_file = db
    
    # Write new object
    with open(FILE, 'w') as file:
      json.dump(temp_file, file, indent=2)

  except Exception as exc:
    print(exc)


  print(f'{L_GREEN}Register:{END} The user has been {L_CYAN}added{END}')


# print(f'\n\n{CYAN}[{END}*{CYAN}]{END} Searching for PHP installation...')


if __name__ == "__main__":
  setDefault()
  main()