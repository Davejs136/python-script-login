""" 
  Este script permitira lo siguiente: 
  - Crear login (Usuario y contraseña)
  - A ese usuario se le permitira crear, eliminar y ocultar carpeta
      dandole roles, accediendo a tales permisos
"""

import json
from os import system
from getpass import getpass
from modules import json_template, file_path

main_message = """
WELCOME TO MY SCRIPT!!!

What options we have ?

1 --------------------> Login
2 --------------------> Register
3 --------------------> About
4 --------------------> Quit

Please enter a option:
"""

print(main_message)

while True:  
  option = input('> ')

  if not option:
    system('clear')
    print('Enter option: ')

  elif option == '4':
    system('clear')
    print('Exit script')
    break


def comprobate_data(json):
  get_user = input('Please enter your user: ')
  get_pass = getpass(prompt='Enter your password: ')

  for x in json:
    name = x['name']
    passwd = x['password']

    if get_user == name and get_pass == passwd:
      print(f'Welcome {name}')
    else:
      print('This user does not exists')
      break

# Comprobate if file exists
try:
  if open(file_path):
    with open(file_path) as json_file:
      json_file_loaded = json.load(json_file)
      comprobate_data(json_file_loaded)

except FileNotFoundError as NotFound:

# Insert first data
  with open(file_path, 'w') as json_file:
    json.dump(json_template, json_file)